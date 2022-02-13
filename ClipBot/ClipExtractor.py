"""
Method that downloads the top clips from r/livestreamfails using the Twitch and Reddit API keys

"""

import os
import sys
import urllib.request

import requests


def extract():
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
    # Insert into URLS links to the top clips from Livestream Fails
    for post in lsfres.json()['data']['children']:
        url = post['data']['url']
        if url.startswith("https://clips.twitch.tv/"):
            URLS.append(url)

    counter = 0
    # For each clip in URLS, try to download it using the twitch API and save it to Videos
    for index, clip in enumerate(URLS):
        if counter < 5:
            basepath = 'Videos/'
            slug = clip.rpartition('/')[-1]
            clip_info = requests.get("https://api.twitch.tv/kraken/clips/" + slug,
                                     headers={"Client-ID": 'gp762nuuoqcoxypju8c569th9wz7q5',
                                              "Accept": "application/vnd.twitchtv.v5+json"}).json()

            try:
                thumb_url = clip_info['thumbnails']['medium']
                mp4_url = thumb_url.split("-preview", 1)[0] + ".mp4"
                out_filename = "clip" + str(counter) + ".mp4"
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
                    print("An exception occurred when trying to download this clip")
                counter += 1

            except:
                print("An exception accured when trying to download this clip")
