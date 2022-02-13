"""
Method that takes videos, uses AssemblyAI to produce subtitles for the videos
and then outputs the videos with subtitles included

"""

import os
from time import sleep

import moviepy.editor as mp
import requests


def caption():
    auth_key = 'c61f276a614a4416a8e9287b02812296'

    transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

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

    # Select all videos that have been extracted
    videos_dir = os.listdir('Videos/')
    videos = [clip for clip in videos_dir if clip.endswith(".mp4")]
    clips_n = len(videos)

    if not os.path.exists("Audios"):
        os.makedirs("Audios")

    if not os.path.exists("Subtitles"):
        os.makedirs("Subtitles")

    # Create audio files from videos
    for i in range(clips_n):
        clip = mp.VideoFileClip(r'Videos/clip' + str(i) + ".mp4")
        clip.audio.write_audiofile(r"Audios/clip" + str(i) + ".mp3")

    # Use AssemblyAI to transcribe audio files and then get the subtitles
    for i in range(clips_n):
        print("Clip No. " + str(i))
        upload_response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers,
                                        data=read_file('Audios/clip' + str(i) + ".mp3"))
        audio_url = upload_response.json()["upload_url"]

        transcript_request = {'audio_url': audio_url, 'filter_profanity': True, }
        transcript_response = requests.post("https://api.assemblyai.com/v2/transcript", json=transcript_request,
                                            headers=headers)
        _id = transcript_response.json()["id"]

        polling_response = requests.get("https://api.assemblyai.com/v2/transcript/" + _id, headers=headers)
        print(polling_response.json()['status'])

        # Waiting for AssemblyAI to process the Video
        while polling_response.json()['status'] != 'completed':
            sleep(3)
            polling_response = requests.get(transcript_endpoint + "/" + transcript_response.json()['id'],
                                            headers=headers)
            print("File is", polling_response.json()['status'])

        print('Creating Subtitles')
        endpoint = "https://api.assemblyai.com/v2/transcript/{}/srt".format(_id)
        response = requests.get(endpoint, headers=headers)

        # Write subtitles into srt file
        f = open("Subtitles/srt{}.srt".format(i), "w+")
        f.write(response.text)
        f.close()

    if not os.path.exists("Output"):
        os.makedirs("Output")

    # put subtitles on videos
    for i in range(clips_n):
        print("Putting together Subtitles and video")
        os.system(
            "ffmpeg -y -i Videos/clip{}.mp4 -b:v 900k -b:a 192k  "
            "-vf subtitles=Subtitles/srt{}.srt Output/out{}.mp4".format(i, i, i))
