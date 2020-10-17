import config
import pprint
import sys
import json
from googleapiclient.discovery import build

my_api_key = config.api_key

def youtube_data(video_id):
    service=build("youtube", "v3", developerKey=my_api_key)
    result = service.videos().list(part='snippet', id=video_id).execute()
    return result

if __name__ == '__main__':
    result = youtube_data(sys.argv[1])
    with open('youtube_data/'+sys.argv[1]+".json", 'w') as videoFile:
        json.dump(result, videoFile)
