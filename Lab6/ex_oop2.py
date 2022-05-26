"""
Student Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

# class attributes

class Student:
    major = 'MIT'


    def __init__(self,name,group):
        self.name = name
        self.group = group

    def introduce(self):
        print(f'My name is {self.name}, I\'m in {self.group} and'
              f'studying in {self.major} major.')
std1 = Student('Supinya Sricharoen','MIT211')
std1.introduce()

std2 = Student('Supinya Sricharoen','MIT212')
std2.introduce()

Student.major = 'LM'

std1.introduce()
std2.introduce()

std2.group = 'LM211'
std2.introduce()