import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

os.system('start smb_stage_clear.wav') 
