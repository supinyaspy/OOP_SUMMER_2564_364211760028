"""
Student Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

class Teacher:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Teacher.')
class Student:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f'My name is {self.name}, I am Student.')

mylist = []
t = Teacher('Supinya Sricharoen')
s = Student('Supinya Sri')

mylist.append(t)
mylist.append(s)

#print(len(mylist))

for x in mylist:
    x.introduce()