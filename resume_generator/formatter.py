def format_personal(personal):
    name = personal.get('name', 'Unknown')
    email = personal.get('email', 'N/A')
    phone = personal.get('phone', 'N/A')
    address = personal.get('address', 'N/A')
    return f"{name}\n{email} | {phone}\n{address}\n"

def format_education(education):
    edu_str = "Education\n"
    for edu in education:
        edu_str += f"{edu.get('degree', 'N/A')} in {edu.get('major', 'N/A')}, {edu.get('institution', 'N/A')}, {edu.get('year', 'N/A')}\n"
    return edu_str

def format_experience(experience):
    exp_str = "Work Experience\n"
    for exp in experience:
        exp_str += f"{exp.get('title', 'N/A')} at {exp.get('company', 'N/A')}, {exp.get('location', 'N/A')}\n"
        exp_str += f"{exp.get('start_date', 'N/A')} - {exp.get('end_date', 'N/A')}\n"
        exp_str += f"{exp.get('description', 'N/A')}\n\n"
    return exp_str

def format_skills(skills):
    return "Skills\n" + ", ".join(skills) + "\n"

def format_personal_md(personal):
    name = personal.get('name', 'Unknown')
    email = personal.get('email', 'N/A')
    phone = personal.get('phone', 'N/A')
    address = personal.get('address', 'N/A')
    return f"# {name}\n\n{email} | {phone}\n\n{address}\n\n"

def format_education_md(education):
    edu_str = "## Education\n\n"
    for edu in education:
        edu_str += f"- **{edu.get('degree', 'N/A')} in {edu.get('major', 'N/A')}**, {edu.get('institution', 'N/A')}, {edu.get('year', 'N/A')}\n"
    return edu_str

def format_experience_md(experience):
    exp_str = "## Work Experience\n\n"
    for exp in experience:
        exp_str += f"### {exp.get('title', 'N/A')} at {exp.get('company', 'N/A')}, {exp.get('location', 'N/A')}\n\n"
        exp_str += f"{exp.get('start_date', 'N/A')} - {exp.get('end_date', 'N/A')}\n\n"
        exp_str += f"{exp.get('description', 'N/A')}\n\n"
    return exp_str

def format_skills_md(skills):
    return "## Skills\n\n" + "\n".join([f"- {skill}" for skill in skills]) + "\n"