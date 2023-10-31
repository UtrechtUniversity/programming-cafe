# Set the initial timeLeft value
timeLeft <- 5

# Countdown loop
while (timeLeft > 0) {
  cat(timeLeft, sep = '')
  Sys.sleep(1)
  timeLeft <- timeLeft - 1
}

shell.exec("smb_stage_clear.wav")