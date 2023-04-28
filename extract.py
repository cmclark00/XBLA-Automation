import os
import patoolib
import shutil

# Get the user's home directory
home_dir = os.path.expanduser("~")

# Get the path to the XBLA folder
xbla_dir = os.path.join(home_dir, "XBLA")

# Get the path to the XBLA_Unpacked folder
xbla_unpacked_dir = os.path.join(home_dir, "XBLA_Unpacked")

# Create the XBLA_Unpacked folder if it doesn't exist
if not os.path.exists(xbla_unpacked_dir):
    os.mkdir(xbla_unpacked_dir)

# Iterate over all of the RAR archives in the XBLA folder
for archive in os.listdir(xbla_dir):
    if archive.endswith(".rar"):
        if not os.path.exists(os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_"))):
            os.mkdir(os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_")))

        # Unpack the archive to the XBLA_Unpacked folder
        patoolib.extract_archive(os.path.join(xbla_dir, archive),
                                 outdir = (os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_"))))

        # Get the path to the innermost subdirectory
        for subdir, dirs, files in os.walk(xbla_unpacked_dir):
            for file in files:
    # Get the path to the innermost file in each subdirectory
                innermost_file = os.path.join(subdir, file)
        

        # Get the name of the extensionless file in the innermost subdirectory
        extensionless_file = innermost_file

        # Rename the extensionless file to match the name of the archive it came from
        os.rename(os.path.join(extensionless_file), os.path.join(xbla_unpacked_dir, archive.replace(".rar", ".pirs")))

        # Delete the innermost directory
        shutil.rmtree(os.path.join(xbla_unpacked_dir, archive[:-4].replace(" ", "_")))
        
        #Remove the .pirs extension
        for subdir, dirs, files in os.walk(xbla_unpacked_dir):
            for file in files:
                src = file
                dst = file.replace(".pirs", " ")
                os.rename(os.path.join(xbla_unpacked_dir, src), (os.path.join(xbla_unpacked_dir, dst)))
            

# Print a message to let the user know that the operation was successful
print("Unpacking complete!")