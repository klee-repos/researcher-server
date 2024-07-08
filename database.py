import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_API_KEY")

supabase: Client = create_client(url, key)


class Database():

    async def create_research(self, research_id):
        data = {
            "uuid": str(research_id),
            "status": "processing",
        }
        response = supabase.table("research").insert(data).execute()
        return response

    async def add_research(self, research_id, result_json):
        data = {
            "status": "completed",
            "research_summary": result_json["research_summary"],
            "hot_takes": result_json["hot_takes"],
            "target_audience": result_json["target_audience"],
            "channels": result_json["channels"],
        }
        response = supabase.table("research").update(
            data).eq("uuid", research_id).execute()
        print(response)
        return

    async def get_research(self):
        response = supabase.table("research").select("*").execute()
        return response

    async def get_research_by_id(self, research_id):
        response = supabase.table("research").select(
            "*").eq("uuid", research_id).execute()
        return response

    async def update_research_status(self, research_id, status):
        data = {
            "status": status
        }
        response = supabase.table("research").update(data).eq(
            "uuid", research_id).execute()
        return response
