import json
from formatter import (
    format_personal, format_education, format_experience, format_skills,
    format_personal_md, format_education_md, format_experience_md, format_skills_md
)


def generate_resume(data, format_type='txt'):
    """Generate a resume in the specified format (txt or md)."""
    if format_type == 'txt':
        resume = format_personal(data['personal'])
        resume += "\n"
        resume += format_education(data['education'])
        resume += "\n"
        resume += format_experience(data['experience'])
        resume += "\n"
        resume += format_skills(data['skills'])
    elif format_type == 'md':
        resume = format_personal_md(data['personal'])
        resume += "\n"
        resume += format_education_md(data['education'])
        resume += "\n"
        resume += format_experience_md(data['experience'])
        resume += "\n"
        resume += format_skills_md(data['skills'])
    else:
        raise ValueError("Unsupported format type")
    return resume


def main():
    # Load JSON data
    with open('resume.json', 'r') as f:
        data = json.load(f)

    # Generate and save .txt resume
    resume_txt = generate_resume(data, 'txt')
    with open('resume.txt', 'w') as f:
        f.write(resume_txt)
    print("Resume generated as resume.txt")

    # Generate and save .md resume
    resume_md = generate_resume(data, 'md')
    with open('resume.md', 'w') as f:
        f.write(resume_md)
    print("Resume generated as resume.md")


if __name__ == "__main__":
    main()