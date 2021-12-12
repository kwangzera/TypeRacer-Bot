# TypeRacer-Bot
Python program that allows the use of both sending keys and simulating keypresses to type at incredibly fast speeds in TypeRacer. Be aware that the effectiveness of the program will depend on latency.

![race](https://github.com/Togohogo1/TypeRacer-Bot/blob/master/screenshots/race.png)\
![interactive](https://github.com/Togohogo1/TypeRacer-Bot/blob/master/screenshots/interactive.png)

### Setup
A webdriver (downloads are available for [Chrome](https://chromedriver.chromium.org/downloads), [Firefox](https://github.com/mozilla/geckodriver/releases), [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), and more) is necessary for the program to run. Installed driver `.exe` files should be placed in a new folder called `TypeRacer-Bot/drivers`. If the webdrivers fail to work, it probably means that either the browser version is not compatible with the webdriver version and/or the browser for the webdriver isn't installed.

To start the program, double click `run.bat` once downloaded. All necessary libraries will be installed in a virtual environment.

### Racing
Anytime a race starts, the user is asked to input a delay time. After entering the delay, one of the two methods of typing, `send_text()` or `press_text()`, will be used.

If using `send_text()`, the delay can be entered before the race starts because the program will automatically send the text to the input box when it is detected. This method is the one currently used in the program.

If using `press_text()`, the delay must be entered as soon as the races start, and the input box must be manually selected before the program starts to simulate keypresses.

In `main()`, `link` can be modified to open an invite link, `delay` can be modified to set a new default delay time, and `driver` can be modified to change the driver to either `"chrome"`, `"firefox"`, or `"edge"`.

### Todo
- Perhaps make the bot more automatic
- Efficiently implement more settings and display them
- Display webdriver versions on README
