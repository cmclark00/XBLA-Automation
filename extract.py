
from pathlib import Path
from fileinput import filename
import os
import os.path
import shutil
from subprocess import run
import patoolib
# Changes ~ to /home/usernam
HomePath = os.path.expanduser('~')
UnpackedPath = ('/XBLA_Unpacked/')
FileName = ""

# this sets FileName to the name of the file in /home/username/XBLA as a string and removes the [] and ''
AllDirs = os.listdir(HomePath + '/XBLA/')

for i in range(len(AllDirs)):
    FileName = AllDirs[i].replace('[', '').replace(']', '').replace("'", '')
# This should check if there is already the same named directory in XBLA_Unpacked folder and if not will create it
   
    MyDir = (FileName)
    Check_Folder = os.path.isdir(str(HomePath + UnpackedPath + MyDir))

    if not Check_Folder:

        os.makedirs(str(HomePath + UnpackedPath + MyDir))
        print("Created Folder : ", MyDir)

    else:
        print(MyDir, "Folder already exists.")
# This extracts the rar in the XBLA folder to XBLA_Unpacked
    patoolib.extract_archive(HomePath + "/XBLA/" + (FileName),
                             outdir= HomePath + UnpackedPath + (FileName))

# This changes the top level directory to removethe .rar from folder name
    
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
            '[', '').replace(']', '').replace("'", ''))

# This sets FileName to correct name with a / for the path and then grabs the next directory name
    FileName = FileName + '/'
    LevelOne = Path(HomePath + UnpackedPath + FileName)
    LevelTwo = Path(HomePath + UnpackedPath + FileName + FileName)
    LevelThree = Path(HomePath + UnpackedPath + FileName + FileName + FileName)
    LevelFour = Path(HomePath + UnpackedPath + FileName + FileName + FileName + FileName)
    DirectoryList = os.listdir(LevelTwo)
    
        
# This changes the 2nd subdirectory to the correct name
    for filename in DirectoryList:
        path = LevelTwo
        src = filename
        dst = FileName[:-1]
        os.rename(os.path.join(path, src), os.path.join(path, dst))

# This grabs the next directory name
    DirectoryList = os.listdir(LevelThree)


# This changes the 3rd subdirectory to the correct name
    for filename in DirectoryList:
        path = LevelThree
        src = filename
        dst = FileName[:-1]
        os.rename(os.path.join(path, src), os.path.join(path, dst))
# This launches wxPirs and tells the user to run it on the correct file then close it
    input("Press Enter to launch wxPirs. Once launched, select the innermost file of " +
          FileName[:-1] + " and close wxPirs")
    run("wxpirs.exe")

# This renames default.xex to the correct FileName.xex
    for filename in DirectoryList:
        path = LevelFour
        filename = "default.xex"
        src = filename
        dst = FileName[:-1] + ".xex"
        os.rename(os.path.join(path, src), os.path.join(path, dst))

# This gets rid of the extra folders by moving everything to the top level directory
        source = LevelFour
        destination = LevelOne
        AllFiles = os.listdir(source)
        for f in AllFiles:
            src = os.path.join(source, f)
            dst = os.path.join(destination, f)
            os.rename(src, dst)
        if i == len(AllDirs) - 1:
            Delete = input("Would you like the original Rar files to be deleted? Enter Y for yes, or N for no: ")
            if Delete == "Y":
                shutil.rmtree(HomePath + "/XBLA")
                os.makedirs(HomePath + "/XBLA") 
                print("Files deleted. The program has finished running.")
            else:
                quit("The program has finished running.")
                

        shutil.rmtree(source)
        shutil.rmtree(LevelThree)
        shutil.rmtree(LevelTwo)
        
        i = i + 1

        
       