import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_API_KEY")

supabase: Client = create_client(url, key)


class Database():

    def insert_research(self, result_json, table_name):
        data = {
            "research_summary": result_json["research_summary"],
            "hot_takes": result_json["hot_takes"],
            "target_audience": result_json["target_audience"],
            "channels": result_json["channels"],
        }
        response = supabase.table(table_name).insert(data).execute()
        return response
