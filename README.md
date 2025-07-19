# KodeCampTask4 - Python Utility Collection

This repository contains three Python utility applications designed to help with common tasks: file organization, student grade management, and resume generation.

## Projects Overview

### 📁 File Organizer
A Python script that automatically organizes files in a directory by their file extensions into categorized folders.

**Location**: `file_organizer/`

**Features**:
- Organizes files by extension (Images, Documents, Others)
- Creates folders automatically
- Handles file conflicts gracefully
- Error handling for file operations

### 📊 Student Report Card
A comprehensive student grade management system that allows you to add, view, and update student records with automatic grade calculation.

**Location**: `student_report_card/`

**Features**:
- Add new students with multiple subjects
- View student records with calculated averages and grades
- Update existing student records
- Persistent data storage using JSON files
- Automatic grade calculation (A-F scale)

### 📄 Resume Generator
A flexible resume generator that creates professional resumes from structured JSON data in multiple formats.

**Location**: `resume_generator/`

**Features**:
- Generate resumes in both text and Markdown formats
- JSON-based data input for easy editing
- Professional formatting
- Modular design with separate formatter functions

## Getting Started

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only standard library)

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd KodeCampTask44
   ```

2. Navigate to any project directory and run the respective Python script:
   ```bash
   # File Organizer
   cd file_organizer
   python organizer.py
   
   # Student Report Card
   cd student_report_card
   python main.py
   
   # Resume Generator
   cd resume_generator
   python resume.py
   ```

## Project Structure
```
KodeCampTask44/
├── file_organizer/
│   ├── organizer.py
│   └── README.md
├── student_report_card/
│   ├── main.py
│   ├── student.py
│   └── README.md
├── resume_generator/
│   ├── resume.py
│   ├── formatter.py
│   ├── resume.json
│   └── README.md
└── README.md
```

## Usage

Each project is self-contained and can be run independently. Refer to the individual README files in each project directory for detailed usage instructions.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the MIT License.