from googlesearch import search


def search_queries(search_query):

    results = list()
    for result in search(search_query, num_results=5):
        print(result)
        results.append(result)
    return results


if __name__ == "__main__":
    query = "IBM watsonx governance documentation"
    json_result = search_queries(query)
    print(json_result)
