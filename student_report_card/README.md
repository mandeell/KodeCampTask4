# Student Report Card System

A comprehensive Python application for managing student grades and generating report cards with automatic grade calculation and persistent data storage.

## Features

- **Student Management**: Add, view, and update student records
- **Multi-Subject Support**: Track scores across multiple subjects
- **Automatic Calculations**: Calculates averages and assigns letter grades
- **Persistent Storage**: Saves student data in JSON format
- **Grade Scale**: Standard A-F grading system
- **Interactive Menu**: User-friendly command-line interface

## Grade Scale

| Average Score | Letter Grade |
|---------------|--------------|
| 90-100        | A            |
| 80-89         | B            |
| 70-79         | C            |
| 60-69         | D            |
| Below 60      | F            |

## Usage

### Running the Application

```bash
python main.py
```

### Main Menu Options

```
Student Report Card App
1. Add Student
2. View Student
3. Update Student
4. Exit
```

### Adding a New Student

1. Select option `1` from the main menu
2. Enter the student's name
3. Add subjects and scores:
   - Enter subject name (or 'done' to finish)
   - Enter the score for that subject
   - Repeat for all subjects
4. Student data is automatically saved

**Example**:
```
Enter student's name: John Doe
Enter subject (or 'done' to finish): Math
Enter score for Math: 85
Enter subject (or 'done' to finish): Science
Enter score for Science: 92
Enter subject (or 'done' to finish): done
Student John Doe added successfully.
```

### Viewing Student Records

1. Select option `2` from the main menu
2. Enter the student's name
3. View complete report including:
   - All subjects and scores
   - Calculated average
   - Letter grade

**Example Output**:
```
Student: John Doe
Subjects and Scores:
Math: 85
Science: 92
Average: 88.50
Grade: B
```

### Updating Student Records

1. Select option `3` from the main menu
2. Enter the student's name
3. Add new subjects or update existing scores
4. Changes are automatically saved

## File Structure

```
student_report_card/
├── main.py          # Main application with menu system
├── student.py       # Student class definition
├── data/           # Auto-created directory for student files
│   ├── john_doe.json
│   ├── jane_smith.json
│   └── ...
└── README.md
```

## Data Storage

Student data is stored in JSON files within the `data/` directory:

- **File naming**: `{student_name_lowercase_with_underscores}.json`
- **Auto-creation**: The `data/` directory is created automatically
- **Format**: Human-readable JSON with proper indentation

**Example JSON structure**:
```json
{
    "name": "John Doe",
    "scores": {
        "Math": 85,
        "Science": 92,
        "English": 78
    },
    "average": 85.0,
    "grade": "B"
}
```

## Class Structure

### Student Class (`student.py`)

**Attributes**:
- `name`: Student's full name
- `scores`: Dictionary of subject-score pairs
- `average`: Calculated average score
- `grade`: Letter grade based on average

**Methods**:
- `add_score(subject, score)`: Add or update a subject score
- `calculate_average()`: Calculate the average of all scores
- `determine_grade()`: Assign letter grade based on average
- `to_dict()`: Convert student object to dictionary
- `from_dict(data)`: Create student object from dictionary

## Requirements

- Python 3.6 or higher
- Standard library modules: `os`, `json`

## Error Handling

The application includes error handling for:
- Duplicate student names (prevents overwriting)
- Non-existent student records
- Invalid menu choices
- File I/O operations

## Features in Detail

### Automatic Grade Calculation
- Recalculates average whenever scores are added or updated
- Immediately assigns appropriate letter grade
- Handles empty score lists gracefully

### Data Persistence
- All student data is automatically saved to JSON files
- No manual save operation required
- Data persists between application sessions

### Flexible Subject Management
- Add unlimited subjects per student
- Update existing subject scores
- Subject names are automatically title-cased for consistency

## Example Workflow

1. **Start the application**: `python main.py`
2. **Add students**: Create records for multiple students with their subjects and scores
3. **View reports**: Check individual student performance
4. **Update records**: Add new subjects or modify existing scores as needed
5. **Data persistence**: All changes are automatically saved and available in future sessions