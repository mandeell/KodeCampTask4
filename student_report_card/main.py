import os
import json
from student import Student

DATA_DIR = 'data'

def save_student(student):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    filename = os.path.join(DATA_DIR, f"{student.name.lower().replace(' ', '_')}.json")
    with open(filename, 'w') as f:
        json.dump(student.to_dict(), f, indent=4)
    print(f"Student {student.name} saved to {filename}")

def load_student(name):
    filename = os.path.join(DATA_DIR, f"{name.lower().replace(' ', '_')}.json")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return Student.from_dict(data)
    else:
        print(f"No data found for student {name}")
        return None