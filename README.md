# TypeRacer-Bot
Python program that allows the use of both sending keys and simulating key presses to cheat in TypeRacer. Be aware that the effectiveness of the program will depend on latency.  

![race](https://github.com/Togohogo1/TypeRacer-Bot/blob/master/screenshots/race.png)  
![interactive](https://github.com/Togohogo1/TypeRacer-Bot/blob/master/screenshots/interactive.png)  

### Setup
A webdriver is necessary for the program to run. If the one located in `TypeRacer-Bot/driver` does not work then [downloads](https://chromedriver.chromium.org/downloads) are available here. Webdrivers are also available for other browsers, but those have not been implemented in this program.

To start the program, double click `run.bat` once downloaded. All necessary libraries will be installed in a virtual environment.

### Racing
Anytime a race starts, the user is asked to input a delay time. If nothing or something invalid is inputted, then the delay time defaults to 0.1s per characters. During the race, one of the two methods of typing, `keysend_type()` and `keypress_type()` will be used.

If using `keypress_type()`, the delay can be entered before the race starts because the program will automatically send the text to the inputbox when it is detected. This automatic method results in lower speeds with more lag.

If using `keysend_type()`, the delay must be entered as soon as the races starts, and the inputbox must be manually selected before the program starts to simulate keypresses. This manual method results in higher speeds with less lag.

In addition, the `link` and `delay` variables can be modified to open an invite link and change the default delay time.

### Todo
- Add drivers for other web browsers
- Perhaps make the bot more automatic
- Add more settings and display them
