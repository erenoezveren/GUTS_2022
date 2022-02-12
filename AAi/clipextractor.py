
"""
Python script which downloads the top clips from livestreamfails using the Twitch and Reddit API keys

"""

import os
import sys
import requests
import urllib.request
import argparse

auth = requests.auth.HTTPBasicAuth('BLuYjxErXU1iGIooZq1hfw', 'xpWGDzNAzXmT3TzYa9o79w1lEMgXlA')
data = {'grant_type': 'password',
        'username': 'natefrostmd',
        'password': 'guts2022password'}

headers = {'User-Agent': 'app by u/natefrostmd'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

lsfres = requests.get("https://oauth.reddit.com/r/livestreamfails/hot",
                   headers=headers)

URLS = []

for post in lsfres.json()['data']['children']:
    url = post['data']['url']
    if url.startswith("https://clips.twitch.tv/"):
        URLS.append(url)

#URLS now contains links to the top clips from Livestream Fails, which we can use twitchdownloader.py to download clips from:

#run os command to download clips:
counter=0

for index, clip in enumerate(URLS):
    if counter<5:
        client_id = 'Your Client ID'
        basepath = 'tmp/'
        slug = clip.rpartition('/')[-1]
        clip_info = requests.get("https://api.twitch.tv/kraken/clips/" + slug, headers={"Client-ID": 'gp762nuuoqcoxypju8c569th9wz7q5', "Accept":"application/vnd.twitchtv.v5+json"}).json()

        try:
            thumb_url = clip_info['thumbnails']['medium']
            mp4_url = thumb_url.split("-preview",1)[0] + ".mp4"
            out_filename = "clip" + str(index) + ".mp4"
            output_path = (basepath + out_filename)


            def dl_progress(count, block_size, total_size):
                percent = int(count * block_size * 100 / total_size)
                sys.stdout.write("\r...%d%%" % percent)
                sys.stdout.flush()

            # create the basepath directory
            if not os.path.exists(basepath):
                os.makedirs(basepath)

            try:
                urllib.request.urlretrieve(mp4_url, output_path, reporthook=dl_progress)
            except:
                print("An exception occurred")
            counter+=1                
        except:
            pass