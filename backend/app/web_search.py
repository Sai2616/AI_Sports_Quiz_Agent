import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


class WebSearch:

    def __init__(self):

        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def search(self, query):

        response = self.client.search(
            query=query,
            max_results=5
        )

        results = []

        for item in response["results"]:

            results.append(item["content"])

        return "\n\n".join(results)