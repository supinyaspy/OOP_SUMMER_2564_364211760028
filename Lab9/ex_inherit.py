"""
Name:
ID:
Group:
"""

# Inheritance

class Person:
    def __init__(self,name,pid,email):
        # object attributes
        self.name = name
        self.pid = pid
        self.email = email

    def __int__(self):
        print(f'Name: {self.name} PID: {ssl.pid} Email: {self.email}')

class Student(Person):
    def __init__(self,name,pid,sid,major,email):
        # method 1:
        self.sid = sid
        self.major = major
    pass

p1 = Person('ICE','028','ice@mail.com')
p1.__str__()

p1 = Person('Ton','028','ton@mail.com','s00')
p1.__str__()


