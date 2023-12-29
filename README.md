# omori-gif-creator
An application that lets you easily create omori gifs with text

pyinstaller --onefile -w --add-data "aubrey:aubrey" --add-data "basil:basil" --add-data "kel:kel" --add-data "omori:omori" --add-data "sunny:sunny" --add-data "output.gif:." --add-data "Arial_Bold.ttf:." --add-data "arial.ttf:." --icon=ologo.png main.py
