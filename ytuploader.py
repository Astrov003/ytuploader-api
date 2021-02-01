from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)



request_body = {
    'snippet':{
        'categoryId': 19,
        'title': 'fairy',
    },
    'status': {
        'privacyStatus': 'private',
    }
}

mediaFile = MediaFileUpload('fairy.mp4')

response_upload = service.videos().insert(
    part = 'snippet, status',
    body = request_body,
    media_body = mediaFile
).execute()
