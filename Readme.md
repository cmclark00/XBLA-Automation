# XBLA-Automation 1.3

## Purpose:
### The purpose of this script is to extract, move, and organize all of your XBLA game archives for easy integration into EmulationStation Desktop Edition

## Why it's necessary:
### The way that Xbox Live Arcade games were packaged was kind of weird. They were stored in a pirs container, which is like a weird archive format that only the xbox 360 used. In the past ES-DE couldnt see these files because they dont actually have a file extension. Now That it can it is much easier to organize your XBLA library using this tool.

## How it works:
### The way the script works is by calling the patoolib module to extract the archives from the input folder you specify to the output folder you specify.
### It then renames the innermost file, the pirs file, to the name of the top level directory, which is your game name.
### Next it moves the newly renamed pirs file to the output folder and deletes the original directory that the pirs file was in.
### Now you should have a nice clean folder full of all of your XBLA games organized, named correctly, and without any unnecessary junk.
### The final step is all on you, it's time to move all of the game folders over to your Roms/xbox 360 folder in your EmulationStation DE directory.

Prerequisites:

Make sure you have a modern version of Python 3 installed, you can check this with python --version in the command line.
Make sure you have some kind of unarchiving program that can handle Rar files.

Instructions for use:

In the command line install the required python modules using "pip install -r requirements.txt".

Download the zipped project file and extract all of its contents.

Place all of your archived XBLA games in one folder, I recommend naming it XBLA.
If the archive name doesn't match the title of the game then fix that now.

Open a command line wherever you extracted the project file to and run "python3 extract.py". Alternatively, run "python3 extractGUI.py" for the GUI version.
The program is now fully automated so you can just sit back and watch it work!



