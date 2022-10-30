# XBLA-Automation 0.2b

## Purpose:
### The purpose of this script is to extract, move, and organize all of your XBLA game archives for easy integration into EmulationStation Desktop Edition

## Why it's necessary:
### Due to the way that XBLA games are packaged ES-DE can't normally recognize the games as being in your Roms/xbox 360 folder. This is because XBLA games are packaged in a pirs file which is only used for the xbox 360, and which have no file extension, which ES-DE uses to recognize the game files. It is possible to do all of the work this program does by hand, it's just a little tedious.

## How it works:
### The way the script works is by calling the patoolib module to extract the archives from the XBLA folder to the XBLA_Unpacked folder.
### At this point there is code in place to rename all of the subdirectories in the directory created from the archive to match the main directory. 
### Finally, the code will rename the default.xex file to the same name as the main directory and then do some subdirectory cleanup by moving all of the game files up a few levels into that main directory and deleting any unused and unnecessary subdirectories and files.
### At this point the program will ask if you want it to delete the original Rar archives for you. If you enter "Y" the program will delete the archives and give a confirmation message and end, otherwise the program will give a termination message.
### Now you should have a nice clean folder full of all of your XBLA games organized, named correctly, and without any unnecessary junk.
### The final step is all on you, it's time to move all of the game folders over to your Roms/xbox 360 folder in your EmulationStation DE directory.

## Important note: When scraping in ES-DE make sure you use thegamesDB as your source, for some reason ScreenScraper doesn't seem towork well with these files.



Prerequisites:
Make sure you have a modern version of Python 3 installed, you can check this with python --version in the command line.
Make sure you have some kind of unarchiving program that can handle Rar files.

Instructions for use:

In the comand line install patool using "pip install patool".
Also install pynput the same way.

Download the zipped project file and extract all of its contents to your home directory.
In Windows this is usually C:\Users\username.
In Linux this is usually /home/username.

Delete the text files named delete me from both the XBLA and XBLA_Unpacked folders.

Place all of your archived XBLA games in the XBLA folder.
If the archive name doesn't match the title of the game then fix that now.

Open a command line in your home directory and run "python3 extract.py"
The program is now fully automated so you can just sit back and watch it work!

Now you can move all of the game folders over to your Roms/xbox 360 folder in your EmulationStation DE setup and run the scraper.

### If you need to run the script again make sure the XBLA_Unpacked folder is empty. If it isn't empty the script will crash.

Special note for Linux users, you will have to use wine to run wxPirs. Linux is not currently supported because wxPirs does some weird things when ran through wine. I am working on it, but since Xenia doesn't officially support linux either at the moment it just isn't a priority.
