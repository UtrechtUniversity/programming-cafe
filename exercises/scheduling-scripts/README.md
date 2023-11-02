# README

## Description
We have selected a couple of exercises to play with your systems internal clock and scheduling tasks.
This folder contains a folder called `scripts` that contains an R and a Python script that you can use to schedule a countdown timer. The scripts will play a sound file when the countdown timer reaches zero. The sound file is located in the `data` folder.
Depending on your skill level and your interest in the topic there are several routes that you can choose.

## Routes
1. Read a tutorial about scheduling tasks in [Windows](https://adamtheautomator.com/cron-for-windows), [Mac](https://medium.com/@justin_ng/how-to-run-your-script-on-a-schedule-using-crontab-on-macos-a-step-by-step-guide-a7ba539acf76) or [Linux](https://itsfoss.com/cron-job/) and schedule the countdown timer script to run at a specific time. **Make sure you read the tips for your specific operating system at the bottom of this page.**

2. Open [this chapter from Automate the Boring Stuff](https://automatetheboringstuff.com/2e/chapter17/), and read and program the examples from the following sections:
    - The Time Module including the stop watch (stop at Rounding Numbers)
    - Project: Simple Countdown Program (use the sound file from the data folder)
    - **The examples are written in Python. We can help you translate the code to R if you want to, or you can try to use the `reticulate` R package.**

3. Open [this chapter from Automate the Boring Stuff](https://automatetheboringstuff.com/2e/chapter17/), and do everything (or the parts you are interested in). Suggestions:
    - The chapters mentioned above
    - The datetime module
    - Converting Strings into datetime Objects
    - Multithreading
    - Passing Arguments to the Thread’s Target Function
    - **The examples are written in Python. We can help you translate the code to R if you want to, or you can try to use the `reticulate` R package.**




## Tips

### MAC

Mac uses the command `open`` to open files and applications from the 'Terminal'. You can use this command to open the sound file of your choice from the 'Terminaĺ' from within R or Python. 

In R you can use the system command to run a command in the MAC terminal. The resulting line of R code looks like this:

```system('open ../data/smb_stage_clear.wav'')```

In Python 

```subprocess.Popen(['open', '../data/smb_stage_clear.wav'])```

### Linux

Linux in most cases does not have a default application to open sound files from the 'Terminal'. You can use `sox` to play sound files from the 'Terminal'.

[Crontab Guru](https://crontab.guru/) is a great website to help you schedule tasks in Linux. 

Open a terminal and use the following commands to install `sox`: 

```sudo apt install sox```
```sudo apt install libsox-fmt-mp3```

After installing `sox` you can use the following command to play a sound file from the 'Terminal':

```play ../data/smb_stage_clear.wav```

In R you can use the system command to run a command in the Linux terminal. The resulting line of R code looks like this:

```system('play ../data/smb_stage_clear.wav')```

In Python 

```subprocess.Popen(['play', '../data/smb_stage_clear.wav'])```
