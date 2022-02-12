import os
import sys
import requests
import urllib.request
import argparse
import requests
import pprint
import json
import moviepy.editor as mp
from time import sleep
import os



auth_key = 'c61f276a614a4416a8e9287b02812296'

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_auth_only = {'authorization': auth_key}

headers = {
    "authorization": auth_key,
    "content-type": "application/json"}

def read_file(filename):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(5242880)
            if not data:
                break
            yield data
arr=os.listdir('tmp/')

for i in range(len(arr)):
    clip = mp.VideoFileClip(r'tmp/clip'+str(i)+".mp4")
    clip.audio.write_audiofile(r"mp/clip"+str(i)+".mp3")


ar = os.listdir('mp/')

for index, clip in enumerate(ar):
    upload_response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file('mp/'+clip))
    audio_url = upload_response.json()["upload_url"]

    transcript_request = {'audio_url': audio_url}
    transcript_response = requests.post("https://api.assemblyai.com/v2/transcript", json=transcript_request, headers=headers)
    _id = transcript_response.json()["id"]


    polling_response = requests.get("https://api.assemblyai.com/v2/transcript/" + _id, headers=headers)
    print(polling_response.json()['status'])


    while polling_response.json()['status'] != 'completed':
        sleep(3)
        polling_response = requests.get(transcript_endpoint+"/"+transcript_response.json()['id'], headers=headers)
        print("File is", polling_response.json()['status'])


    print('Creating subtitles')
    endpoint = "https://api.assemblyai.com/v2/transcript/{}/srt".format(_id)
    response = requests.get(endpoint, headers=headers)
    f = open("subtitles/srt{}.srt".format(index), "w+")
    f.write(response.text)
    f.close()

#put subtitles on videos
for i in range(len(arr)):
    print("PuTTING SUbTiTlES")
    os.system("ffmpeg -y -i tmp/clip{}.mp4 -vf subtitles=subtitles/srt{}.srt out/out{}.mp4".format(i,i,i))

