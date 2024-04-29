# WARNING: THE COMMAND IN THE LAST LINE OF THIS SCRIPT WILL DIFFER IF YOU ARE USING MAC OR LINUX
# CHECK THE README OF THE EXERCISES FOR TIPS

# Set the initial timeLeft value
timeLeft <- 5

# Countdown loop
while (timeLeft > 0) {
  cat(timeLeft, sep = '')
  Sys.sleep(1)
  timeLeft <- timeLeft - 1
}

shell.exec("../data/smb_stage_clear.wav")