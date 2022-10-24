import os
import pip
import patoolib

Castle_Crashers = ("Castle_Crashers")
Check_Folder= os.path.isdir(Castle_Crashers)

if not Check_Folder:
    os.makedirs(Castle_Crashers)
    print("Created Folder : ",Castle_Crashers)

else:
    print(Castle_Crashers, "Folder already exists.")

patoolib.extract_archive("/home/corey/Downloads/CC.rar", outdir="/home/corey/Documents/Castle_Crashers")