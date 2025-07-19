# File Organizer

A Python utility that automatically organizes files in a directory by sorting them into folders based on their file extensions.

## Features

- **Automatic File Sorting**: Organizes files by extension into predefined categories
- **Smart Folder Creation**: Creates destination folders automatically if they don't exist
- **Conflict Handling**: Skips files that already exist in the destination to prevent overwrites
- **Error Handling**: Gracefully handles file operation errors
- **User-Friendly**: Interactive prompts for folder path input

## Supported File Types

The organizer currently supports the following file categories:

| Extension | Destination Folder |
|-----------|-------------------|
| `.jpg`, `.png` | Images |
| `.docx`, `.pdf` | Documents |
| All others | Others |

## Usage

1. **Run the script**:
   ```bash
   python organizer.py
   ```

2. **Enter the folder path** when prompted:
   ```
   Enter the path of the folder to organize: /path/to/your/folder
   ```

3. **Watch the magic happen**: The script will:
   - Check if the folder exists
   - Create category folders (Images, Documents, Others)
   - Move files to their appropriate folders
   - Display progress messages

## Example

```bash
$ python organizer.py
Enter the path of the folder to organize: C:/Users/Downloads
Moved photo1.jpg to Images
Moved document.pdf to Documents
Moved report.docx to Documents
Moved unknown_file.xyz to Others
File existing_photo.jpg already exists in Images. Skipping.
```

## File Structure After Organization

```
Your Folder/
├── Images/
│   ├── photo1.jpg
│   └── photo2.png
├── Documents/
│   ├── document.pdf
│   └── report.docx
└── Others/
    └── unknown_file.xyz
```

## Customization

To add support for more file types, modify the `file_types` dictionary in `organizer.py`:

```python
file_types = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.mp3': 'Audio',      # Add new types
    '.mp4': 'Videos',     # Add new types
    '.txt': 'Text Files'  # Add new types
}
```

## Requirements

- Python 3.6 or higher
- Standard library modules: `os`, `shutil`

## Error Handling

The script includes robust error handling for:
- Non-existent folder paths
- File permission issues
- File operation failures
- Existing files in destination folders

## Safety Features

- **Non-destructive**: Files are moved, not copied, preserving disk space
- **Conflict prevention**: Existing files are not overwritten
- **Validation**: Checks folder existence before processing
- **Detailed feedback**: Shows exactly what actions were taken