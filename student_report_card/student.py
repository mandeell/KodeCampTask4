import json

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}  # Dictionary with subject: score pairs
        self.average = 0
        self.grade = ''

    def add_score(self, subject, score):
        self.scores[subject] = score
        self.calculate_average()
        self.determine_grade()

    def calculate_average(self):
        if self.scores:
            self.average = sum(self.scores.values()) / len(self.scores)
        else:
            self.average = 0

    def determine_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def to_dict(self):
        return {
            'name': self.name,
            'scores': self.scores,
            'average': self.average,
            'grade': self.grade
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['name'])
        student.scores = data['scores']
        student.average = data['average']
        student.grade = data['grade']
        return student