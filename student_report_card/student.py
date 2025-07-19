import json

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}  # Dictionary with subject: score pairs
        self.average = 0
        self.grade = ''

    def add_score(self, subject, score):
        self.scores[subject] = score