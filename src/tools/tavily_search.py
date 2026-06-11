from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def tavily_search(query:str)->str:

    response = client.search(query=query,max_results=3)

    results = []

    for item in response["results"]:
        results.append(
            f"Title : {item['title']}\n"
            f"Content : {item['content']}\n"
        )
    
    return "\n\n".join(results)