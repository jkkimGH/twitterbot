from serpapi import GoogleSearch

def getImage(word):

    params = {
    "q": word,
    "tbm": "isch",
    "ijn": "0",
    "tbs": "il:cl",
    "api_key": "" # <-- Your API key goes here
    } 

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']
    
    return images_results
