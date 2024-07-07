import uvicorn
import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crew import TheCrew
from pydantic import BaseModel

app = FastAPI()

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


@app.get("/")
def read_root():
    return {"message": "What would you like to research today?"}


@app.post("/research")
async def research(request: ResearchRequest):
    print(request.topic)
    the_crew_instance = TheCrew()
    result = the_crew_instance.start_crew(request.topic)
    json_string = json.loads(result)
    return json_string


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
