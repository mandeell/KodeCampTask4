import os
import shutil

# Define file types and their corresponding folders
file_types = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.docx': 'Documents',
    '.pdf': 'Documents'
}

def get_folder_path():
    """Prompt the user for the folder path to organize."""
    return input("Enter the path of the folder to organize: ")


def main():
    # Get folder path from user
    folder_path = get_folder_path()

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Get file extension (lowercase)
            extension = os.path.splitext(filename)[1].lower()
            # Determine destination folder (default to 'Others' if not in file_types)
            dest_folder = file_types.get(extension, 'Others')
            dest_path = os.path.join(folder_path, dest_folder)

            # Create destination folder if it doesn't exist
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

if __name__ == "__main__":
    main()