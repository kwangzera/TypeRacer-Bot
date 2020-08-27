# TypeRacer-Bot
This TypeRacer Bot uses both selenium and keyboard input with beautifulsoup4 to simulate key presses.  
Be aware that the effectiveness of the program will depend on latency.  

### Setup
Once downloaded, double click `run.bat` to start the program.  
All necessary libraries will be installed in a virtual environment.  

### Background
Text finding will be done by using the webdriver to get the HTML of the current page.  
Beautifulsoup4 will then be used instead of selenium to retrieve the text since selenium can be slow sometimes.  

### Usage
**This program is not fully automatic as it does require you to do some clicking around. Automation is only for typing purposes.**

### Todo
- Add drivers not just for chrome
- More intuitive and automatic interface
