from django.shortcuts import render

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import facebook

import subprocess

import cv2
import time
from django.http import StreamingHttpResponse
from .models import User, Video

# Create your views here.
def stream(request):
    return render(request, 'live_stream/stream.html')
def startYoutubeStream(request):
    # Path to your service account JSON file
    SERVICE_ACCOUNT_FILE = 'F:\Data Analyst\Django\DSE\DseAnalysis/live-stream-392607-a2dbfd356e69.json'
    
    # Scopes required for YouTube API
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    
    # Authenticate with YouTube API using service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    youtube = build('youtube', 'v3', credentials=credentials)
    
    try:
        # Start live streaming on YouTube
        # Set appropriate values for the 'snippet' and 'cdn' parameters
        # based on your specific requirements
        # response = youtube.liveBroadcasts().insert(
        #     part='snippet,cdn',
        #     body={
        #         'snippet': {
        #             'title': 'My Live Stream Title',
        #             'description': 'Description of my live stream',
        #         },
        #         'cdn': {
        #             'resolution': '720p',
        #             'ingestionType': 'rtmp',
        #         }
        #     }
        # ).execute()

        response = youtube.liveBroadcasts().insert(
        part='snippet',
        body={
            'snippet': {
                'title': 'My Live Stream Title',
                'description': 'Description of my live stream',
            }
        }
        ).execute()
        
        # Retrieve the YouTube live stream ID
        stream_id = response['id']
        
        # Render a template with the YouTube stream ID
        return render(request, 'live_stream/youtube-live-stream.html', {'stream_id': stream_id})
    
    except HttpError as e:
        # Handle any HTTP errors
        error_message = e.content.decode("utf-8")
        return render(request, 'live_stream/youtube-live-stream.html', {'error_message': error_message})
    #return render(request, 'live_stream/youtube-live-stream.html')

s_id = ""
def startFacebookStream(request):
   # Your Facebook app credentials
    app_id = '119171507898458'
    app_secret = '0e4659c28e1fba8c66db27829853f099'
    page_access_token = 'EAABsYsdlSFoBAFGkOP0dq1AaeWkIdbineKnsxZBJLIhWf7lPB8Y4C9ntkDfo3p2mLsddWiIC1FKlvObZA1EFKcocVw94EBFhVqGEbCxGI8ZBAzuFCPlrM5GzgC8YLJIabBcliA3SL4JKu63EGCM7VwznyR2twRG5ttJKxd3S9iM4mVApmd2'

    # Authenticate with Facebook API
    fb = facebook.GraphAPI(access_token=page_access_token)

    try:
        # Start the Facebook Live stream on the Page
        response = fb.put_object(parent_object='100471329793121', connection_name='live_videos',
                                 title='My Live Stream Title', description='Description of my live stream')

        print("Response",response)
        # Retrieve the Facebook Live stream ID
        stream_id = response['id']

        # Render a template with the Facebook stream ID
        return render(request, 'live_stream/facebook-live-stream.html', {'stream_id': stream_id})

    except facebook.GraphAPIError as e:
        # Handle any Graph API errors
        error_message = str(e)
        return render(request, 'live_stream/facebook-live-stream.html', {'error_message': error_message})
    #return render(request, 'live_stream/facebook-live-stream.html')

# def stopFacebookStream(request):
#     # Authenticate with Facebook API
#     fb = facebook.GraphAPI(access_token='EAABsYsdlSFoBAGfVjBo33fta0hvhIphl4NOZBeU0FuDYpwrMfk0GqRBE6MSATKGWFFeKmF2aZCUtNRI4LIc6a7rdpTglqVPqEnEthtfi9WirLhp6ZBGNflB6GI8ULZBHB3MBKnyooRNpzxGWjJ924sKGCBySaWmOXvzZB7ZACo6UEVRjRIQHzx')
    
#     # Stop the Facebook live stream
#     fb.delete_object(id=s_id)
    
#     # Render a template to indicate that the stream has been stopped
#     return render(request, 'live_stream/facebook-live-stream.html', {'stream_id': s_id})
#     #return render(request, 'live_stream/facebook-live-stream.html')


# Function to capture frames from the camera using OpenCV
def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Decorator to enable Gzip compression for the video stream
# @gzip.gzip_page
# def live_stream(request, user_id):
#     try:
#         user = User.objects.get(user_id=user_id)
#         return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace;boundary=frame")
#     except User.DoesNotExist:
#         return render(request, 'error.html', {'message': 'User does not exist'})