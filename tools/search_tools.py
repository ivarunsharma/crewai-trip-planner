import requests
from crewai.tools import tool


class SearchTools:

    @tool("Search the internet")
    def search_internet(query: str):
        """Search the internet for the given query and return top results."""
        url = "https://google.serper.dev/search"

        payload = {
            "q": query
        }

        headers = {
            "X-API-KEY": "REMOVED",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()

        results = []

        if "organic" in data:
            for result in data["organic"][:5]:
                results.append(result["title"] + " : " + result["link"])

        return "\n".join(results)