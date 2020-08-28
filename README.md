# TypeRacer-Bot
Python program that allows the use of both sending keys and simulating key presses to cheat in TypeRacer.  
Be aware that the effectiveness of the program will depend on latency.  

### Setup
Once downloaded, double click `run.bat` to start the program.  
All necessary libraries will be installed in a virtual environment.  

### Racing
Anytime a race starts, the user is asked to input a delay time. If nothing or something invalid is inputted, than the delay time defaults to 0.1s per characters. During the race, one of the two methods of typing, `keysend_type()` and `keypress_type()` will be used.

If using `keypress_type()`, the delay can be entered before the race starts because the program will automatically send the text to the inputbox when it is detected. This automatic method results in lower speeds with more lag.

If using `keysend_type()`, the delay must be entered as soon as the races starts, and the inputbox must be manually selected before the program starts to simulate keypresses. This manual method results in higher speeds with less lag.

In addition, the `link` variable can be modified to open an invite link and `delay` can be modified to change the default delay time.

### Todo
- Add drivers for other web browsers
- Perhaps make the bot more automatic
