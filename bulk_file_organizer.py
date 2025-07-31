import os
import shutil
import re
from datetime import datetime

def organize_files(source_dir, dest_dir, prefix="File", organize_by_type=True):
    """Rename and organize files in a source directory."""
    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # File type to folder mapping
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.pdf', '.docx', '.txt'],
        'videos': ['.mp4', '.mov', '.avi'],
        'others': []
    }

    # Counter for renaming
    file_count = 1

    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        if os.path.isfile(src_path):
            # Get file extension
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            # Determine destination folder based on file type
            if organize_by_type:
                for folder, extensions in file_types.items():
                    if ext in extensions:
                        dest_folder = os.path.join(dest_dir, folder)
                        break
                else:
                    dest_folder = os.path.join(dest_dir, 'others')
            else:
                dest_folder = dest_dir

            # Create destination folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # Create new filename with timestamp and counter
            timestamp = datetime.now().strftime("%Y%m%d")
            new_filename = f"{prefix}_{timestamp}_{file_count:03d}{ext}"
            dest_path = os.path.join(dest_folder, new_filename)

            # Rename and move file
            shutil.move(src_path, dest_path)
            print(f"Moved and renamed: {filename} -> {new_filename}")

            file_count += 1

def main():
    # Configuration
    source_directory = r"C:\Users\ASUS\Documents\College\SEMESTER 2"  # Folder with messy files
    destination_directory = r"C:\Users\ASUS\Documents\College\SEMESTER 2\organized"  # Where files will be organized
    prefix = "Task"  # Prefix for renamed files
    organize_by_type = True  # Organize into subfolders by file type

    # Run organizer
    organize_files(source_directory, destination_directory, prefix, organize_by_type)
    print("File organization completxe!")

if __name__ == "__main__":
    main()