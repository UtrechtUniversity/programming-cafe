# WARNING: THE COMMAND IN THE LAST LINE OF THIS SCRIPT WILL DIFFER IF YOU ARE USING MAC OR LINUX
# CHECK THE README OF THE EXERCISES FOR TIPS

import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

os.system('start smb_stage_clear.wav') 
