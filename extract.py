
from ast import Str
import os
import pip
import patoolib

FileName = os.listdir('/home/corey/Downloads')
FileName = (str(FileName).replace('[','').replace(']','').replace("'",''))
  
MyDir = (FileName)
Check_Folder= os.path.isdir(str(FileName))

if not Check_Folder:
    os.makedirs(str(FileName))
    print("Created Folder : ", FileName)

else:
    print(FileName, "Folder already exists.")

patoolib.extract_archive("/home/corey/Downloads/" + str(FileName), outdir="/home/corey/Documents/" + str(FileName))