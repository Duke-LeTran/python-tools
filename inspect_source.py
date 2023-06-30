import subprocess
import os
import pandas as pd

# Get the path of the pandas module
pandas_path = os.path.dirname(pd.core.frame.__file__)

# Open the folder in File Explorer
subprocess.run(['explorer', pandas_path])

##################################
# For more than operating system
##################################
import platform

def open_folder(folder_path):
    # Get the platform (e.g., 'Windows', 'Linux', 'Darwin')
    operating_system = platform.system()

    command_map = {
        'Windows': ['explorer', folder_path],
        'Linux': ['xdg-open', folder_path],
        'Darwin': ['open', folder_path]
    }

    command = command_map.get(operating_system)

    if command is not None:
        subprocess.run(command)
    else:
        print('Opening folders is not supported on this platform.')

# Specify the folder path you want to open
folder_path = '/path/to/folder'

# Open the folder
open_folder(folder_path)