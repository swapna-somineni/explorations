import requests


def get_wikipedia_content(title):
    WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,  # Fetch only the introduction
        "titles": title
    }
    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()

    return data


if __name__ == "__main__":
    title = "IBM"

    json_result = get_wikipedia_content(title)
    print(json_result)
    page = next(iter(json_result["query"]["pages"].values()))
    print(f"Title: {page['title']}\n")
    print(f"Summary:\n{page['extract']}")
