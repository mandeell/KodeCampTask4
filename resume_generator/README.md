# Resume Generator

This project generates a resume from structured JSON data in both `.txt` and `.md` formats.

## Usage

1. Edit `resume.json` with your personal information, education, experience, and skills.
2. Run `python resume.py` to generate `resume.txt` and `resume.md`.

## JSON Schema

The `resume.json` file should contain:
- `personal`: name, email, phone, address
- `education`: list of degrees with degree, major, institution, year
- `experience`: list of jobs with title, company, location, start_date, end_date, description
- `skills`: list of skills

See `resume.json` for an example.

## Output
- `resume.txt`: Plain text resume
- `resume.md`: Markdown resume