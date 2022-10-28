
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
PackedPath = ('/XBLA/')
FileName = ""


def renameLevelDir(List):
    for filename in os.listdir(List):
        srcDir = filename
        dstDir = FileName[:-1]
        os.rename(os.path.join(List, src), os.path.join(List, dst))

# This gets all of the archives from XBLA and sets FileName to the name of the file in /home/username/XBLA as a string and removes the [] and ''
AllDirs = os.listdir(HomePath + PackedPath)
for i in range(len(AllDirs)):
    FileName = AllDirs[i].replace('[', '').replace(']', '').replace("'", '')

# This creates the directory to unRar into
    os.makedirs(str(HomePath + UnpackedPath + FileName))

# This extracts the rar in the XBLA folder to XBLA_Unpacked
    patoolib.extract_archive(HomePath + PackedPath + (FileName),
                             outdir=HomePath + UnpackedPath + (FileName))

# This changes the top level directory to removethe .rar from folder name
    DirectoryList = os.listdir(HomePath + UnpackedPath)

# !!Warning: This sets FileName to the last folder in DirectoryList
# If there are multiple folders, only the last one will be saved to FileName
    for filename in DirectoryList:
        # set parent path
        path = HomePath + UnpackedPath

        # Set FileName var, as this will be valid in the end anyways
        FileName = filename.replace('.rar', '')
        
        # set source and dest
        src_folder = os.path.join(path, filename)
        dst_folder = os.path.join(path, FileName)

        # check if dest already exists, delete if it does
        if os.path.isdir(dst_folder):
            shutil.rmtree(dst_folder)

        # move source to dest
        try:
            os.rename(src_folder, dst_folder)
        except:
            print(f'Unable to move {src_folder} to {dst_folder}')

    # This grabs the new correct name and set FileName to that
        FileName = (str(FileName).replace(
            '[', '').replace(']', '').replace("'", ''))

      # This sets FileName to correct name with a / for the path and then grabs the next directory name, while also creating the level structure for paths
        FileName = FileName + '/'
        Levels = [HomePath + UnpackedPath + FileName]
        Levels = [x + FileName * ii for x in Lists for ii in range(4)]

        # This changes the 2nd subdirectory to the correct name
        renameLevelDir(Lists.at(1))
        # This changes the 3rd subdirectory to the correct name
        renameLevelDir(Lists.at(2))

    # This launches wxPirs and tells the user to run it on the correct file then close it
        input("Press Enter to launch wxPirs. Once launched, select the innermost file of " +
              FileName[:-1] + " and close wxPirs")
        run("wxpirs.exe")

    # This renames default.xex to the correct FileName.xex
        for filename in DirectoryList:
            filename = "default.xex"
            src = filename
            dst = FileName[:-1] + ".xex"
            os.rename(os.path.join(Lists.at(3), src), os.path.join(Lists.at(3), dst))

    # This moves everything to the top level directory
            destination = Lists.at(0)
            AllFiles = os.listdir(Lists.at(3))
            for f in AllFiles:
                src = os.path.join(Lists.at(3), f)
                dst = os.path.join(destination, f)
                os.rename(src, dst)

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

    # This deletes all of the extra subdirectories inside the game directories
            for xx in range(1,4):
                shutil.rmtree(Lists.at(xx))
