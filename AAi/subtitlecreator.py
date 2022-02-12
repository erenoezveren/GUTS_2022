import cv2
import pandas as pd
from moviepy.editor import VideoFileClip
import math

def create_pipeline():
    def pipeline(gf, t):
        try:
            print(t)
            print(type(t))
            cv2.putText(gf(t), timestamps_better.get(math.floor(t*1000),""), (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, cv2.LINE_AA)

        except StopIteration:
            pass
        # additional frame manipulation
        return gf(t)

    timestamps = extract_timestamps("id1.txt")
    video = VideoFileClip("tmp/DeadLovelyNoodleTheTarFu-V7soR_a1A-EPT2C2.mp4")

    out_video = video.fl(pipeline, apply_to='mask')
    out_video.write_videofile("vidout.mp4", audio=True)

def extract_timestamps(file):
    timestamps = {}
    f = open(file, "r")
    #remove header
    f.readline()
    f.readline()

    timestamp = f.readline()[:-1]
    while(timestamp):
        timestamps[timestamp] = f.readline()[:-1]
        f.readline()
        timestamp = f.readline()[:-1]

    #very descriptive
    global timestamps_better
    timestamps_better = {}
    for timestamp,phrase in timestamps.items():
        print(timestamp)
        beginning = turn_time_into_int(timestamp[3:9])
        end = turn_time_into_int(timestamp[17:])
        for i in range(beginning,end):
            timestamps_better[i]=phrase

def turn_time_into_int(t):
    int_t = int(t.replace(".",""))
    return int_t

if __name__ == "__main__":
    create_pipeline()
    extract_timestamps("id1.txt")