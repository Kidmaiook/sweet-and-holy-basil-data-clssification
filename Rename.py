import os

def rename_files_in_folder(folder_path, prefix, start_num):
    """
    Renames all files in a given folder by adding a prefix and a sequential number.

    Args:
        folder_path (str): The path to the folder containing the files.
        prefix (str): The prefix to add to the new file names.
        start_num (int): The starting number for the sequential count.
    """
    try:
        # Get a list of all items in the folder
        items = os.listdir(folder_path)
        
        # Filter out directories, keeping only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]
        
        # Sort files to ensure consistent renaming order (optional but recommended)
        files.sort()
        
        print(f"Found {len(files)} files to rename in '{folder_path}'...")
        
        # Iterate through the files and rename them
        for index, old_name in enumerate(files):
            # Construct the full old file path
            old_file_path = os.path.join(folder_path, old_name)
            
            # Separate the filename from its extension
            name, extension = os.path.splitext(old_name)
            
            # Create the new file name: prefix + sequential number + original extension
            new_name = f"{prefix}{start_num + index}{extension}"
            
            # Construct the full new file path
            new_file_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            print(f"  Renamed: '{old_name}' -> '{new_name}'")
            
        print("\n✅ Renaming complete!")

    except FileNotFoundError:
        print(f"\n❌ Error: The folder path '{folder_path}' was not found.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# --- Configuration ---
# ⚠️ IMPORTANT: Change this to the path of the folder you want to modify!
folder_to_rename = os.path.join("Foldercoding/Sweet_basil") 
# e.g., "C:/Users/YourName/Desktop/Images" or "/home/user/documents/data"

# Optional: Customize the prefix and starting number
file_prefix = "SB" 
start_number = 1

rename_files_in_folder(folder_to_rename, file_prefix, start_number)