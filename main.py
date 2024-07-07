import uvicorn
import os
import json
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crew import TheCrew
from pydantic import BaseModel
from database import Database

load_dotenv()

app = FastAPI()

os.environ["OPENAI_API_KEY"] = "NA"

# List of allowed origins (you can use "*" to allow all)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str


async def start_crew_async(topic: str):
    the_crew_instance = TheCrew()
    result = the_crew_instance.start_crew(topic)
    try:
        cleaned_string = result.replace("```json", "").replace("```", "")
        result_json = json.loads(cleaned_string)
        response = Database().insert_research(result_json, "research")
        return response
    except:
        return result


@app.get("/")
def read_root():
    return {"message": "What would you like to research today?"}


@app.post("/research")
async def research(request: ResearchRequest):
    asyncio.create_task(start_crew_async(request.topic))
    return {"status": "processing..."}


@app.get("/test")
def test():
    test_string = "```json\n{\n  \"research_summary\": \"The research summary focuses on the go-to-market strategy for electric cars, targeting environmentally conscious individuals and early technology adopters. This includes millennials, Gen Z, and businesses seeking sustainable alternatives. Demographic factors, such as age, interests, and geographic locations, will be utilized for targeted digital ads. The summary emphasizes the need to create engaging content, build thought leadership, and leverage various channels to reach the target audience effectively.\",\n  \"hot_takes\": [\n    \"Electric cars are the future, and we're bringing them to the present with a strategy that speaks to the conscious consumer.\",\n    \"Say goodbye to range anxiety and hello to sustainable adventures with our upcoming electric car models!\",\n    \"Are you a business seeking to green your fleet? We've got electric car solutions that will rev your engines and lower your carbon footprint.\",\n    \"The electric car revolution is here, and we're charging ahead with innovative technology and eco-friendly designs.\",\n    \"Get ready to plug into a community of forward-thinkers and change-makers with our electric car movement!\"\n  ],\n  \"target_audience\": \"The target audience for this go-to-market strategy related to electric cars is primarily comprised of individuals and organizations who prioritize environmental sustainability and embrace technological advancements. This includes millennials and Gen Z consumers, who are increasingly aware of climate change and its implications. Businesses and institutions seeking ways to reduce their environmental impact and promote eco-friendly initiatives are also key targets. Demographically, we can target younger age groups and those with a demonstrated interest in technology and environmental topics through their online behavior. Additionally, we will focus on geographic locations that have higher adoption rates of electric vehicles, as these areas indicate a stronger acceptance of this technology.\",\n  \"channels\": [\n    \"Social media platforms (Instagram, Twitter, TikTok): Leveraging these platforms allows us to connect with younger demographics through creative content, influencer collaborations, and targeted advertising, ensuring a wide reach and engagement.\",\n    \"Email Newsletters: Building a subscriber base through email newsletters enables direct communication with interested individuals, providing them with educational content, industry updates, and promotions to drive conversions.\",\n    \"Podcasts: Sponsoring or creating podcasts related to sustainability, technology, or the automotive industry will capture the attention of engaged listeners, positioning us as thought leaders and providing in-depth information on electric car benefits.\",\n    \"Online Publications and Blogs: Collaborating with influential platforms in the automotive, technology, or environmental space increases our visibility and credibility, reaching a wider audience through guest contributions and targeted ad placements.\",\n    \"YouTube: Partnering with or creating YouTube channels focused on electric car reviews, battery technology, and sustainable living engages a visually-focused audience, providing an opportunity for demonstrations and building trust through testimonials.\",\n    \"Display Ads: Utilizing display ad networks across multiple websites allows us to target specific demographics and interests, increasing brand awareness and reaching a diverse range of potential customers.\"\n  ]\n}\n```"
    test_string = test_string.replace("```json", "").replace(
        "```", "")
    result_json = json.loads(test_string)
    print(result_json["research_summary"])
    response = Database().insert_research(result_json, "research")
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
