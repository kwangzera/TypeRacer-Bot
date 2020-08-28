# TypeRacer-Bot
Python program that allows the use of both sending keys and simulating key presses to cheat in TypeRacer  
Be aware that the effectiveness of the program will depend on latency.  

### Setup
Once downloaded, double click `run.bat` to start the program.  
All necessary libraries will be installed in a virtual environment.  

### Usage
There are several fields that can be modified:
- `keysend_type()`: Enter the text in the inputbox by simulating key presses
- `keypress_type()`: Enter the text in the inputbox by sending keys with selenium
- `link`: Default typeracer link which can be changed to an invite link
- `delay`: Default delay time if user does not specify a delay time at the beginning of each race

If using `keypress_type()`, the delay can be entered before the race starts becuase the program will automatically send the text to the inputbox when it is detected. This automatic method results in lower speeds with more lag.

If using `keysend_type()`, the delay must be entered as soon as the races starts, and the inputbox must be manually selected before the program starts to simulate keypresses. This manual method results in higher speeds with less lag.

### Todo
- Add drivers for other web browsers
- Perhaps make the bot more automatic
