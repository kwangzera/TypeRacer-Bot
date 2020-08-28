# TypeRacer-Bot
This TypeRacer Bot uses both selenium and keyboard input to simulate key presses.  
Be aware that the effectiveness of the program will depend on latency.  

### Setup
Once downloaded, double click `run.bat` to start the program.  
All necessary libraries will be installed in a virtual environment.  

### Usage
Typing the text into the inputbox can be done with `keypress_type()`, which simulates key presses or  `keysend_type()` which uses selenium.  
Before pressing setting your delay speed and pressing enter, make sure a race is counting down. This requires some navigating around the page.  
If using `keypress_type()`, ...  
If using `keysend_type()`, ...  

### Misc
Text finding will be done by using the webdriver to get the HTML of the current page.  
Beautifulsoup4 will then be used instead of selenium to retrieve the text since selenium can be slow sometimes.  

### Todo
- Add drivers for other web browsers
