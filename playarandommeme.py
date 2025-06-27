import subprocess
import os
import random

vids = []

def videotime():
    return random.choice(os.listdir("/home/toll/Videos/memes"))

def play(vids):
    for vid in vids:
        os.system("/bin/vlc /home/toll/Videos/memes/"+vid+" -L --fullscreen")

for _ in range(10):  
    vid = videotime()
    if vid not in vids:
        print(vid)
        vids.append(vid)

play(vids)
