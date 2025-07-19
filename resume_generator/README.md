# Resume Generator

A flexible Python application that generates professional resumes from structured JSON data in multiple formats (text and Markdown). Perfect for creating consistent, well-formatted resumes that can be easily updated and customized.

## Features

- **Multiple Output Formats**: Generate resumes in both plain text (`.txt`) and Markdown (`.md`) formats
- **JSON-Based Input**: Easy-to-edit structured data format
- **Professional Formatting**: Clean, consistent layout for both formats
- **Modular Design**: Separate formatting functions for easy customization
- **Automatic Generation**: Creates both formats simultaneously

## Usage

### Quick Start

1. **Edit your resume data**:
   ```bash
   # Edit the resume.json file with your information
   ```

2. **Generate your resume**:
   ```bash
   python resume.py
   ```

3. **Output files created**:
   - `resume.txt` - Plain text format
   - `resume.md` - Markdown format

### Example Output

The script will display:
```
Resume generated as resume.txt
Resume generated as resume.md
```

## JSON Data Structure

The `resume.json` file should contain the following sections:

### Personal Information
```json
{
  "personal": {
    "name": "Your Full Name",
    "email": "your.email@example.com",
    "phone": "(555) 123-4567",
    "address": "City, State, ZIP"
  }
}
```

### Education
```json
{
  "education": [
    {
      "degree": "Bachelor of Science",
      "major": "Computer Science",
      "institution": "University Name",
      "year": "2020"
    }
  ]
}
```

### Experience
```json
{
  "experience": [
    {
      "title": "Software Developer",
      "company": "Company Name",
      "location": "City, State",
      "start_date": "January 2021",
      "end_date": "Present",
      "description": "Description of responsibilities and achievements"
    }
  ]
}
```

### Skills
```json
{
  "skills": [
    "Python",
    "JavaScript",
    "SQL",
    "Git"
  ]
}
```

## File Structure

```
resume_generator/
├── resume.py          # Main script
├── formatter.py       # Formatting functions
├── resume.json        # Your resume data
├── resume.txt         # Generated plain text resume
├── resume.md          # Generated Markdown resume
└── README.md
```

## Output Formats

### Plain Text Format (`.txt`)
- Clean, readable format suitable for ATS systems
- Consistent spacing and alignment
- Professional layout

### Markdown Format (`.md`)
- GitHub-compatible Markdown
- Enhanced formatting with headers and emphasis
- Easy to convert to HTML or PDF
- Great for online portfolios

## Customization

### Adding New Sections

1. **Update JSON structure**: Add new section to `resume.json`
2. **Create formatter function**: Add formatting function in `formatter.py`
3. **Update main script**: Include new section in `resume.py`

### Modifying Formatting

Edit the formatting functions in `formatter.py`:
- `format_personal()` / `format_personal_md()` - Personal information
- `format_education()` / `format_education_md()` - Education section
- `format_experience()` / `format_experience_md()` - Work experience
- `format_skills()` / `format_skills_md()` - Skills section

## Requirements

- Python 3.6 or higher
- Standard library modules: `json`

## Error Handling

The application includes error handling for:
- Missing or invalid JSON files
- Unsupported format types
- File I/O operations

## Example Complete JSON

```json
{
  "personal": {
    "name": "John Doe",
    "email": "john.doe@email.com",
    "phone": "(555) 123-4567",
    "address": "New York, NY 10001"
  },
  "education": [
    {
      "degree": "Bachelor of Science",
      "major": "Computer Science",
      "institution": "Tech University",
      "year": "2020"
    }
  ],
  "experience": [
    {
      "title": "Software Developer",
      "company": "Tech Corp",
      "location": "New York, NY",
      "start_date": "June 2020",
      "end_date": "Present",
      "description": "Developed web applications using Python and JavaScript"
    }
  ],
  "skills": [
    "Python",
    "JavaScript",
    "React",
    "SQL",
    "Git"
  ]
}
```

## Tips for Best Results

1. **Keep descriptions concise**: Use clear, action-oriented language
2. **Update regularly**: Keep your JSON file current with new experiences
3. **Proofread**: Review generated resumes for accuracy
4. **Customize per job**: Modify skills and descriptions for specific applications
5. **Version control**: Use Git to track changes to your resume data

## Future Enhancements

Potential improvements will include:
- PDF output format
- Custom styling options
- Template selection
- Web-based interface
- Integration with job boards