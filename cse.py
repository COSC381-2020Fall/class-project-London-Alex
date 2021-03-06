import config
from pprint import pprint
from googleapiclient.discovery import build

my_api_key = config.api_key
my_cse_id = config.cse_id
my_search_topic = 'Continental Divide'

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

if __name__ == '__main__':
    resultsList = []
    for x in range(10):
        index=x*10+1
        results = google_search(my_search_topic, my_api_key, my_cse_id, num=10, start=index)
        resultsList.append(results)
    pprint(resultsList)    
