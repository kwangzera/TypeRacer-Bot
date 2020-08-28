# TypeRacer-Bot
This TypeRacer Bot uses both selenium and keyboard input to simulate key presses.  
Be aware that the effectiveness of the program will depend on latency.  

### Setup
Once downloaded, double click `run.bat` to start the program.  
All necessary libraries will be installed in a virtual environment.  

### Usage
There are several fields that can be modified:
- `keysend_type()`: 
- `keypress_type()`:
- `link`:
- `delay`:

### Misc
Text finding will be done by using the webdriver to get the HTML of the current page.  
Beautifulsoup4 will then be used instead of selenium to retrieve the text since selenium can be slow sometimes.  

### Todo
- Add drivers for other web browsers
