from pathlib import Path
import os
import os.path
import shutil
import patoolib

# Changes ~ to /home/username
HomePath = os.path.expanduser('~')
UnpackedPath = os.path.join('', 'XBLA_Unpacked')
PackedPath = os.path.join('', 'XBLA')
FileName = ""

# This gets all of the archives from XBLA and sets FileName to the name of the file in /home/username/XBLA/ as a string and removes the [] and ''
AllDirs = os.listdir(os.path.join(HomePath, PackedPath))
for i in range(len(AllDirs)):
    FileName = AllDirs[i].replace('[', '').replace(']', '').replace("'", '')
    
    # This creates the directory to unRar into
    os.makedirs(os.path.join(HomePath, UnpackedPath, FileName.replace(" ", "_")))

    # This extracts the rar in the XBLA folder to XBLA_Unpacked
    patoolib.extract_archive(os.path.join(HomePath, PackedPath, FileName),
                                outdir=os.path.join(HomePath, UnpackedPath, FileName.replace(" ", "_")))
    
    # This changes the top level directory to remove the .rar from folder name
    DirectoryList = os.listdir(os.path.join(HomePath, UnpackedPath))
    for filename in DirectoryList:
        src = filename
        filename = filename.replace('.rar', '')
        dst = filename
        path = os.path.join(HomePath, UnpackedPath)
        os.rename(os.path.join(path, src), os.path.join(path, dst))
        FileName = dst

    # This grabs the new correct name and set FileName to that
    FileName = (str(FileName).replace(
        '[', '').replace(']', '').replace("'", '').replace(" ", "_"))

    # This sets FileName to correct name with a / for the path and then grabs the next directory name, while also creating the level structure for paths
    FileName = FileName.replace(" ", "_") + os.sep
    LevelOne = Path(os.path.join(HomePath, UnpackedPath, FileName))
    LevelTwo = Path(os.path.join(HomePath, UnpackedPath, FileName, FileName))
    LevelThree = Path(os.path.join(HomePath, UnpackedPath, FileName, FileName, FileName))
    LevelFour = Path(os.path.join(HomePath, UnpackedPath, FileName, FileName, FileName, FileName))

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

    # This renames the pirs file to correct filename
    for filename in DirectoryList:
        path = LevelFour
        for root, dirs, files in os.walk(path):
            for file in files:
        # Get the full path to the file
                file_path = os.path.join(root, file)
                filename = os.path.basename(file_path)
                src = filename
                dst = FileName.replace('_', ' ')[:-1] + (".pirs")
                FileName = os.rename(os.path.join(path, src), os.path.join(path, dst))

    # This moves everything to the top level directory
    source = LevelFour
    destination = os.path.join(HomePath, UnpackedPath)
    AllFiles = os.listdir(source)
    for f in AllFiles:
        src = os.path.join(source, f)
        dst = os.path.join(destination, f)
        os.rename(src, dst)

    # This erases the original folder
    DeleteFiles = os.listdir(LevelOne)
    for f in DeleteFiles:
        shutil.rmtree(LevelOne)

    # This removes the pirs extension
    source = os.listdir(os.path.join(HomePath, UnpackedPath))
    for filename in source:
        path = os.path.join(HomePath, UnpackedPath)
        for root, dirs, files in os.walk(path):
            for file in files:
        # Get the full path to the file
                file_path = os.path.join(root, file)        
                src = file_path
                dst = file_path.replace('.pirs','')
                os.rename(src, dst)
    
# This asks the user if they want to delete the original Rar files and does so if they choose Y for yes
if i == len(AllDirs) - 1:
    DeletePath = HomePath + PackedPath
    Delete = input("Would you like the original Rar files to be deleted? Enter Y for yes, or N for no: ")
    if Delete == "Y" or Delete == "y":
        shutil.rmtree(HomePath + "/XBLA")
        os.makedirs(HomePath + "/XBLA")
        print("Files deleted. The program has finished running.")
    else:
        quit("The program has finished running.")


            
        
        