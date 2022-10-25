
from ast import Str
from fileinput import filename
import os
import os.path
from subprocess import run
import patoolib
# Changes ~ to /home/usernam
HomePath = os.path.expanduser('~')
UnpackedPath = ('/XBLA_Unpacked/')
# this sets FileName to the name of the file in /home/username/XBLA as a string and removes the [] and ''
FileName = os.listdir(HomePath + '/XBLA/')
FileName = (str(FileName).replace('[', '').replace(']', '').replace("'", ''))
# This should check if there is already the same named directory in XBLA_Unpacked folder and if not will create it
MyDir = (FileName)
Check_Folder = os.path.isdir(str(HomePath + UnpackedPath + FileName))

if not Check_Folder:
    os.makedirs(str(HomePath + UnpackedPath + FileName))
    print("Created Folder : ", FileName)

else:
    print(FileName, "Folder already exists.")
# This extracts the rar in the XBLA folder to XBLA_Unpacked
patoolib.extract_archive(HomePath + "/XBLA/" + (FileName),
                         outdir=HomePath + "/XBLA_Unpacked/" + (FileName))

# This changes the top level directory to removethe .rar from folder name
DirectoryList = os.listdir(HomePath + UnpackedPath)

for filename in DirectoryList:
    src = filename
    dst = filename[:-4]
    path = HomePath + UnpackedPath
    os.rename(os.path.join(path, src), os.path.join(path, dst))

# This grabs the new correct name and set FileName to that
DirectoryList = os.listdir(HomePath + UnpackedPath)
FileName = DirectoryList
FileName = (str(FileName).replace('[', '').replace(']', '').replace("'", ''))

# This sets FileName to correct name with a / for the path and then grabs the next directory name
FileName = FileName + '/'
DirectoryList = os.listdir(HomePath + UnpackedPath + FileName + FileName)

# This changes the 2nd subdirectory to the correct name
for filename in DirectoryList:
    path = HomePath + UnpackedPath + FileName + FileName
    src = filename
    dst = FileName[:-1]
    os.rename(os.path.join(path, src), os.path.join(path, dst))

# This grabs the next directory name
DirectoryList = os.listdir(HomePath + UnpackedPath +
                           FileName + FileName + FileName)


# This changes the 3rd subdirectory to the correct name
for filename in DirectoryList:
    path = HomePath + UnpackedPath + FileName + FileName + FileName
    src = filename
    dst = FileName[:-1]
    os.rename(os.path.join(path, src), os.path.join(path, dst))
#This launches wxPirs and tells the user to run it on the correct file then close it
run("wxpirs.exe")
input("Press enter after you have used wxPirs on the innermost file of " + FileName + " and closed wxPirs")

#This renames default.xex to the correct FileName.xex
for filename in DirectoryList:
    path = HomePath + UnpackedPath + FileName + FileName + FileName + FileName
    filename = "default.xex"
    src = filename
    dst = FileName[:-1] + ".xex"
    os.rename(os.path.join(path, src), os.path.join(path, dst))

#This gets rid of the extra folders by moving everything to the top level directory
source = HomePath + UnpackedPath + FileName + FileName + FileName + FileName
destination = HomePath + UnpackedPath + FileName
AllFiles = os.listdir(source)
for f in AllFiles:
    src = os.path.join(source, f)
    dst = os.path.join(destination, f)
    os.rename(src, dst)