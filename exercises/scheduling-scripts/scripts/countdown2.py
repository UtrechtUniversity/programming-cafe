#! python3
# countdown.py - A simple countdown script.

import time, subprocess
import os

timeLeft = 5
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
os.system('export DISPLAY=:0 && /usr/bin/play $HOME/Repositories/programming-cafe/exercises/scheduling-scripts/data/smb_stage_clear.wav')