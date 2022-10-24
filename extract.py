
from ast import Str
import os
import os.path
import pip
import patoolib
#Changes ~ to /home/usernam
HomePath = os.path.expanduser('~')
#this sets FileName to the name of the file in /home/username/XBLA as a string and removes the [] and ''
FileName = os.listdir(HomePath + '/XBLA/')
FileName = (str(FileName).replace('[','').replace(']','').replace("'",''))
#This should check if there is already the same named directory in XBLA_Unpacked folder and if not will create it
MyDir = (FileName)
Check_Folder= os.path.isdir(str(HomePath + '/XBLA_Unpacked/' + FileName))

if not Check_Folder:
    os.makedirs(str(HomePath + '/XBLA_Unpacked/' + FileName))
    print("Created Folder : ", FileName)

else:
    print(FileName, "Folder already exists.")
#This extracts the rar in the XBLA folder to XBLA_Unpacked
patoolib.extract_archive(HomePath + "/XBLA/" + (FileName), outdir= HomePath + "/XBLA_Unpacked/" + (FileName))
