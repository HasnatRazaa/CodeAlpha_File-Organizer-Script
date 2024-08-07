import os
import shutil

# Define the source directory
source_directory = r"C:\Users\Administrator\Music"   # Change this to your target directory

# Define the target directory structure
folder_structure = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Others': []
}


def organize_files(source_dir):
    # Create target folders if they don't exist
    for folder in folder_structure.keys():
        folder_path = os.path.join(source_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Move file to the corresponding folder
        moved = False
        for folder, extensions in folder_structure.items():
            if file_extension in extensions:
                target_path = os.path.join(source_dir, folder, filename)
                shutil.move(file_path, target_path)
                print(f"Moved: {filename} to {folder}")
                moved = True
                break

        # If the file type is not recognized, move it to 'Others'
        if not moved:
            target_path = os.path.join(source_dir, 'Others', filename)
            shutil.move(file_path, target_path)
            print(f"Moved: {filename} to Others")


organize_files(source_directory)