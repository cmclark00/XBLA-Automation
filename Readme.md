# XBLA-Automation 0.2b

## The purpose of this script is to extract, move, and organize all of your XBLA game archives for easy integration into EmulationStation Desktop Edition

### How it works:
The way the script works is by calling the patoolib module to extract the archives from the XBLA folder to the XBLA_Unpacked folder.
At this point there is code in place to rename all of the subdirectories in the irectory created from the archive to match the main directory.
After this happens the script will ask the user to hit enter to launch the wxPirs program with a message to select the pirs file in the innermost subdirectory, and
to close the program after that file has been unpacked. The user must hit enter again AFTER they have closed wxPirs.
Finally, the code will rename the default.xex file to the same name as the main directory and then do some subdirectory cleanup by moving all of the game files up a few levels into that main directory.
At this point your terminal should be pointing back at your home directory and you should have nice organized game folders in XBLA_Unpacked.
The final step is all on you, it's time to move all of the game folders over to your Roms/xbox 360 folder in your EmulationStation DE directory.

## Important note: When scraping in ES-DE make sure you use thegamesDB as your source, for some reason ScreenScraper doesn't seem towork well with these files.

Instructions for use:

Make sure you have the newest version of python installed.

In the comand line install patool using "pip install patool".

Download the zipped project file and extract all of its contents to your home directory.
In Windows this is usually C:\Users\username.
In Linux this is usually /home/username.

Delete the text files named delete me from both the XBLA and XBlA_Unpacked folders.

Place all of your archived XBLA games in the XBLA folder.
If the archive name doesn't match the title of the game then fix that now.

Open a command line in your home directory and run "python extract.py"

Keep an eye on the terminal, eventually it will ask you to hit enter to launch wxPirs.
Select the innermost file in the game directory in XBLA_Unpacked by clicking the open button and navigating to it, then click the save/extract button.
Once it is done extracting all of the files close wxPirs and then hit enter in the command line window.
## Very important: Do not hit enter for the second time until after you have closed wxPirs. If wxPirs is still open when you hit enter for the second time the program will crash .

Repeat the last step until you have gone through all of your archives. You will know the program has ended when it shows your home directory as the final location in the terminal.

Now you can move all of the game folders over to your Roms/xbox 360 folder in your EmulationStation DE setup and run the scraper.

### If you need to run the program again make sure the XBLA_Unpacked folder is empty. If it isn't empty the program will crash.

Special note for Linux users, you will have to use wine to run wxPirs. Once you set that up it should run fine.