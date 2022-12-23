"""Every second, checks to see if Rhythmbox is open, and if so, writes the 
currently playing song to a file.
12/12/22
Sharie Rhea"""

import subprocess
import time

"""Returns the currently playing song."""
def getSong():
    output = subprocess.run(["rhythmbox-client", "--print-playing"], 
        capture_output=True)
    return output.stdout.decode("UTF-8").strip()

"""Writes the currently playing song to a file."""
def writeSong():
    file = open("CurrentSong.txt", "w")
    file.write("Music from Gamechops.com      ")
    file.write(getSong())
    file.write("      ")
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

running = checkRhythmbox()
if running:
    prevSong = getSong()
    writeSong()
else:
    quit()

# main loop
while True:
    running = checkRhythmbox()
    if running:
        currSong = getSong()
        if prevSong != currSong:
            prevSong = currSong
            writeSong()
        time.sleep(1)
    else:
        quit()