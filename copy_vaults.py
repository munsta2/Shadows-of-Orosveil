import shutil
import os

import shutil
import os

def copy_folder(source_dir, destination_dir, overwrite=False):
    """
    Copies a folder from the source directory to the destination directory.

    Parameters:
    - source_dir (str): The path to the folder you want to copy.
    - destination_dir (str): The path to the directory where the folder will be copied.
    - overwrite (bool): Whether to overwrite the folder if it already exists in the destination. Defaults to False.
    """
    # Ensure source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    # Define the full destination path for the copied folder
    dest_folder = os.path.join(destination_dir, os.path.basename(source_dir))
    
    # If overwrite is allowed and the folder exists, remove it
    if overwrite and os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    
    # Copy the folder
    try:
        shutil.copytree(source_dir, dest_folder)
        print(f"Folder '{source_dir}' has been copied to '{dest_folder}'.")
    except FileExistsError:
        print(f"Folder '{dest_folder}' already exists. Use overwrite=True to replace it.")

# Example usage:
# copy_folder('/path/to/source_folder', '/path/to/destination', overwrite=True)


# Example usage:
# bulk_copy('/path/to/source', '/path/to/destination', overwrite=True)
copy_folder("D:\Jesse\Documents\Orosveil\World", "D:\Jesse\Documents\quartz\content",True)
copy_folder("D:\Jesse\Documents\Orosveil\Images", "D:\Jesse\Documents\quartz\content",True)
copy_folder("D:\Jesse\Documents\Orosveil\Orosveil Player’s Handbook", "D:\Jesse\Documents\quartz\content",True)