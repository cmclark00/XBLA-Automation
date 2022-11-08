from pathlib import Path
from fileinput import filename
import os
import os.path
import shutil
from subprocess import Popen
import patoolib
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# Changes ~ to /home/usernam
HomePath = os.path.expanduser('~')
UnpackedPath = ('/XBLA_Unpacked/')
PackedPath = ('/XBLA/')
FileName = ""

# This gets all of the archives from XBLA and sets FileName to the name of the file in /home/username/XBLA as a string and removes the [] and ''
AllDirs = os.listdir(HomePath + PackedPath)
for i in range(len(AllDirs)):
    FileName = AllDirs[i].replace('[', '').replace(']', '').replace("'", '')
    
# This creates the directory to unRar into
    os.makedirs(str(HomePath + UnpackedPath + FileName.replace(" ", "_") + ".xex"))

# This extracts the rar in the XBLA folder to XBLA_Unpacked
    patoolib.extract_archive(HomePath + PackedPath + (FileName),
                             outdir=HomePath + UnpackedPath + (FileName.replace(" ", "_") + '.xex'))
    FileName = FileName.replace(" ", "_") + ".xex"

# This changes the top level directory to remove the .rar from folder name
    DirectoryList = os.listdir(HomePath + UnpackedPath)
    for filename in DirectoryList:
        src = filename
        filename = filename.replace('.rar', '')
        dst = filename
        path = HomePath + UnpackedPath
        os.rename(os.path.join(path, src), os.path.join(path, dst))
        FileName = dst

# This grabs the new correct name and set FileName to that
    FileName = (str(FileName).replace(
        '[', '').replace(']', '').replace("'", '').replace(" ", "_"))

# This sets FileName to correct name with a / for the path and then grabs the next directory name, while also creating the level structure for paths
    FileName = FileName.replace(" ", "_") + '/'
    LevelOne = Path(HomePath + UnpackedPath + FileName)
    LevelTwo = Path(HomePath + UnpackedPath + FileName + FileName)
    LevelThree = Path(HomePath + UnpackedPath + FileName + FileName + FileName)
    LevelFour = Path(HomePath + UnpackedPath + FileName +
                     FileName + FileName + FileName)
    
# This sets the 2nd directory to the correct name
    DirectoryList = os.listdir(LevelOne)
    for filename in DirectoryList:
        path = LevelOne
        src = filename
        dst = FileName[:-1]
        os.rename(os.path.join(path, src), os.path.join(path, dst))
    
    

# This changes the 2nd subdirectory to the correct name
    DirectoryList = os.listdir(LevelTwo)
    for filename in DirectoryList:
        path = LevelTwo
        src = filename
        dst = FileName[:-1]
        os.rename(os.path.join(path, src), os.path.join(path, dst))

# This changes the 3rd subdirectory to the correct name
    DirectoryList = os.listdir(LevelThree)
    CorrectDir = '000D0000'
    for filename in DirectoryList:
        path = LevelThree
        src = CorrectDir
        dst = FileName[:-1]
        os.rename(os.path.join(path, src), os.path.join(path, dst))
                
               
            

# This launches wxPirs , picks the correct file, then utomatically unpacks it to the correct location
    
        GetPirs = os.listdir(LevelFour)
        GetPirs = (str(GetPirs).replace(
            '[', '').replace(']', '').replace("'", ''))
        PirsPath = str(LevelFour) + "/" + str(GetPirs)
        RunWxpirs = Popen({'wine', 'wxPirs.exe', PirsPath})
        sleep(3)
        keyboard.press(Key.alt)
        keyboard.release(Key.alt)

        keyboard.press('f')
        keyboard.release('f')

        keyboard.press(Key.down)
        keyboard.release(Key.down)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(15)
        Popen.kill(RunWxpirs) 
        sleep(5)
       
        
        
    # This renames default.xex to the correct FileName.xex
        for filename in DirectoryList:
            path = LevelFour
            filename = "default.xex"
            src = filename
            dst = FileName.replace('_', ' ')[:-1]
            os.rename(os.path.join(path, src), os.path.join(path, dst))

    # This moves everything to the top level directory
            source = LevelFour
            destination = LevelOne
            AllFiles = os.listdir(source)
            for f in AllFiles:
                src = os.path.join(source, f)
                dst = os.path.join(destination, f)
                os.rename(src, dst)

    # This changes the folder name back to game name with no underscores
            DirectoryList = os.listdir(HomePath + UnpackedPath)
            for filename in DirectoryList:
                        path = HomePath + UnpackedPath
                        src = filename
                        dst = filename.replace('_', ' ')
                        os.rename(os.path.join(path, src), os.path.join(path, dst))

    # This deletes all of the extra subdirectories inside the game directories
            LevelFour = HomePath + UnpackedPath + FileName.replace('_', ' ') + FileName + FileName + FileName
            LevelThree = HomePath + UnpackedPath + FileName.replace('_', ' ') + FileName + FileName
            LevelTwo = HomePath + UnpackedPath + FileName.replace('_', ' ') + FileName
            source = LevelFour
            shutil.rmtree(source)
            shutil.rmtree(LevelThree)
            shutil.rmtree(LevelTwo)

    # This asks the user if they want to delete the original Rar files and does so if they choose Y for yes
            if i == len(AllDirs) - 1:
                DeletePath = HomePath + PackedPath
                Delete = input(
                    "Would you like the original Rar files to be deleted? Enter Y for yes, or N for no: ")
                if Delete == "Y":
                    shutil.rmtree(HomePath + "/XBLA")
                    os.makedirs(HomePath + "/XBLA")
                    print("Files deleted. The program has finished running.")
                else:
                    quit("The program has finished running.")



            
        
        