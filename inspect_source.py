import subprocess
import os
import pandas as pd

def open_module_directory():
    # Get the path of the pandas module
    pandas_path = os.path.dirname(pd.core.frame.__file__)
    # Open the folder in File Explorer
    subprocess.run(['explorer', pandas_path])


def open_folder(folder_path):
    """works on more than one operating system"""
    import platform

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


def inspect_function():
    """ This is how you can inspect a function for its parameters"""
    import inspect

    def my_function(arg1, arg2, *args, **kwargs):
        pass

    # Get the function signature
    signature = inspect.signature(my_function)

    # Get the parameters of the function
    parameters = signature.parameters