import PySimpleGUI as sg
import os
import patoolib
import shutil

def unpack_xbla(xbla_dir, xbla_unpacked_dir):
        
        # Iterate over all of the RAR archives in the XBLA folder
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
                        dst = file.replace(".pirs", "")
                        os.rename(os.path.join(xbla_unpacked_dir, src), (os.path.join(xbla_unpacked_dir, dst)))
                
            print(file)



layout = [
    [sg.Text("XBLA Unpacker")],
    [sg.Text("Input Folder")],
    [sg.InputText(key = "Input Folder"), sg.FolderBrowse()],
    [sg.Text("Output Folder")],
    [sg.InputText(key = "Output Folder"), sg.FolderBrowse()],
    [sg.Button("Unpack"), sg.Button("Quit")],
    [sg.ProgressBar(100, orientation="horizontal", size=(20, 20)), sg.Button("Unpack"), sg.Button("Quit")]
]

finished = [
    [sg.Text("The Program Has Finished.")]
]


win = sg.Window("XBLA Unpacker", layout)

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "Quit":
        break
    if event == "Unpack":
        # Unpack the XBLA files
        unpack_xbla(values["Input Folder"], values["Output Folder"])
        break

win.close()

