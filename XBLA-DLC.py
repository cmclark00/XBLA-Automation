import os
import patoolib
import shutil
from alive_progress import alive_bar
import time
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Get the user's home directory
home_dir = os.path.expanduser("~")

# Get the path to the XBLA folder
print("Please choose your input folder: ")
xbla_dir = askdirectory()

# Get the path to the XBLA_Unpacked folder
print("Please choose your output folder: ")
xbla_unpacked_dir = askdirectory()

# Iterate over all of the RAR archives in the XBLA folder
with alive_bar(len(os.listdir(xbla_dir))) as bar:
    for archive in os.listdir(xbla_dir):
        if archive.endswith(".rar"):
            if not os.path.exists(os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_"))):
                os.mkdir(os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_")))

            # Unpack the archive to the XBLA_Unpacked folder
            patoolib.extract_archive(os.path.join(xbla_dir, archive),
                                        outdir = os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_")), verbosity=-1)

            # Get the path to the innermost subdirectory
            for subdir, dirs, files in os.walk(xbla_unpacked_dir):
                for file in files:

            # Check if the file already exists
                    if os.path.exists(os.path.join(xbla_unpacked_dir, file)):
                        continue

            # Rename the file to move it to the root of the xbla_unpacked-dir
                    os.rename(os.path.join(subdir, file), os.path.join(xbla_unpacked_dir, file))



    
        print(file)
        bar()
# Print a message to let the user know that the operation was successful
print("Unpacking complete!")

# Ask if the user wants to delete the .rar archives
deleteRar = ""
while deleteRar != "Y" and deleteRar != "y" and deleteRar != "N" and deleteRar != "n":
    deleteRar = input("Would you like to delete the .rar folder and the .rar archives inside it? Enter Y or N: ")
    if deleteRar == "Y" or deleteRar == "y":
        shutil.rmtree(xbla_dir)
        print(".rar folder has been deleted.")
    else:
        quit