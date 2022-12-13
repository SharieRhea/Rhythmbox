"""Every second, checks to see if Rhythmbox is open, and if so, writes the 
currently playing song to a file.
12/12/22
Sharie Rhea"""

import subprocess
import time

"""Writes the currently playing song to a file."""
def writeSong():
    # get the title and artist from Rhythmbox and format it
    output = subprocess.run(["rhythmbox-client", "--print-playing"], 
        capture_output=True)
    title = output.stdout.decode("UTF-8").strip()
    file = open("CurrentSong.txt", "w")
    file.write(title)
    file.close()

"""Checks to see if Rhythmbox is open, if yes: return True, else: return
False."""
def checkRhythmbox():
    op = subprocess.run(["ps", "-e"], capture_output=True)
    running = op.stdout
    if b"rhythmbox" in running:
        return True
    else:
        return False

while True:
    flag = checkRhythmbox()
    if flag:
        writeSong()
        time.sleep(1)
    else:
        quit()