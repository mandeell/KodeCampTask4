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

def add_student():
    name = input("Enter student's name: ")
    filename = os.path.join(DATA_DIR, f"{name.lower().replace(' ', '_')}.json")
    if os.path.exists(filename):
        print(f"Student {name} already exists. Use update to modify.")
        return
    student = Student(name)
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        score = float(input(f"Enter score for {subject}: "))
        student.add_score(subject.title(), score)
    save_student(student)
    print(f"Student {name} added successfully.")

def view_student():
    name = input("Enter student's name: ")
    student = load_student(name)
    if student:
        print(f"Student: {student.name}")
        print("Subjects and Scores:")
        for subject, score in student.scores.items():
            print(f"{subject}: {score}")
        print(f"Average: {student.average:.2f}")
        print(f"Grade: {student.grade}")
    else:
        print(f"Student {name} not found.")

def update_student():
    name = input("Enter student's name: ")
    student = load_student(name)
    if not student:
        print(f"Student {name} not found.")
        return
    while True:
        subject = input("Enter subject to update/add (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        score = float(input(f"Enter new score for {subject}: "))
        student.add_score(subject.title(), score)
    save_student(student)
    print(f"Student {name} updated successfully.")

def main():
    while True:
        print("\nStudent Report Card App")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()