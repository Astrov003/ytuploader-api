YouTube Uploader


This is a very simple script for uploading videos to YouTube.
I was not satisfied with the applications I downloaded, so I decided to make one myself.

In the testing phase, this is intended to be used privately for my channel. As I continue to learn developing along the way, I hope to turn it into a full application. All the other applications I found had some design decision that did not fit in the flow of uploading, in the sense of it worsening the ease of use. For example, adding is easy, but editing title or description is a pain. Vice versa was the case as well. Some of them were a part of video editors, in the sense of having a too heavy application. I just needed a simple, slick and clean YouTube upload application.

Fully coded in Python at the moment. It is using YouTube Data API v3.

Instructions: (I am writing these instructions as a prototype, because in the test phase only those that I added in my Google Developer Console can use it, right? It does not make a lot of sense now, but still. It is easier to edit this later)

1. I am still not sure about this client_secret.json file. I obtained it from my console, but I am still learning how this works, so I can not provide instructions on this atm.

2. You need to install Python Library 

	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

3. Make sure your account is verified. If not, go to https://www.youtube.com/verify to verify your account.

4. Place "*.mp4" video file in the working directory, and change the line

	mediaFile = MediaFileUpload('fairy.mp4') 
	
to your file name.

5. Run script and login to your channel. Token will be created. Close browser, and run script again to upload the video.

Source Code:
https://github.com/Astrov003/ytuploader-api

Astrov
