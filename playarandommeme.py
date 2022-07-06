import subprocess
import os
import random

def videotime():
    vid = random.choice(os.listdir("/home/toll/Videos/Videos"))
    os.system("/bin/vlc /home/toll/Videos/Videos/"+vid)

for _ in range(10):  
    videotime()