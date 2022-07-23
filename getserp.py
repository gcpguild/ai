import os
api_key_serp =  os.getenv("SERP_API")  # your serpapi api key

print(api_key_serp)

search = "hindu temples in uttar pradesh"

from serpapi import GoogleSearch

params = {
  "q": search,
  "hl": "en",
  "gl": "in",
  "google_domain": "google.co.in",
  "num" : 20,
  "api_key": api_key_serp
}

search = GoogleSearch(params)
results = search.get_dict()

print(results)