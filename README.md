# Game-Launcher (windows)

A simple and minimal game launcher for the terminal.

# Features:

1. Minimal UI
2. Purely for terminal Lovers 🖥️
3. Easy access to games without creating shortcuts on desktop or using Heavy launchers in background to play

# Developer Notes:

This utility is purely depended on built-in python modules, doesn't require any sort of installation of third-party modules
### Modules used
pickle
subprocess
_colorize (some sort of built in module for ANSI escape characters to paint your terminal)
sys
time (for sleep functionality)
pathlib (only for checking path existence)

### Working:

This whole script is totally dependent on a binary file "gamelist.bin" which is automatically created in the "public documents folder" in

` c:\users\public\documents` folder

So, technically this is a fail-safe program, as even if the gamelist gets deleted (or it never existed before) it just creates one. Also, the gamelist stays, so even if you 
delete the program and reinstall your games would be securely stored and you wont need to setup again (its not a very big deal anyway)

The drag and drop feature of terminal allows for the path to be entered in the input field, speaking of which, both `.exe` and `.lnk` (shortcut) file path can be used to run an application 
(since windows 11 allows running shortcut files through terminal directly).

## FEATURES YET TO COME:

1. Rearranging the games to your liking
2. Renaming the games (includes changing the path, the icon)
3. a better UI
4. Color your game names
5. favorites list

## BUILD FROM SOURCE:
`pyinstaller gamelauncher.py --onefile --icon=favicon.ico --name=GAMES`

this should be modified as per your needs. Make sure to install pyinstaller from PyPI.
