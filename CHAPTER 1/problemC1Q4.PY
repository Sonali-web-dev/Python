import os

def list_directory_contents(directory):
    try:
        # List all the files and directories in the given directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")

# Replace this with the path you want to list
directory_path = "."  # "." refers to the current directory
list_directory_contents(directory_path)
