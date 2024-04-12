YOUTUBE_API = "AIzaSyChEr_2TTSeJiOtjWZhw8lGqTFWOBEr3pQ"

from googleapiclient.discovery import build

# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyChEr_2TTSeJiOtjWZhw8lGqTFWOBEr3pQ"
# API client
research = 'road accident, CCTV camera'
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
# Notice that nextPageToken now is requested in 'fields' parameter
request = youtube.search().list(
        part="id,snippet",
        type='video',
        q={research},
        videoDuration='short',
        videoDefinition='high',
        maxResults=10,
        fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
)
response = request.execute()
videos = response['items']
for video in videos:
    print(video['id']['videoId'])
    break
    id = video['id']['videoId']
    title = video['snippet']['title']
    print('title: {title}')
