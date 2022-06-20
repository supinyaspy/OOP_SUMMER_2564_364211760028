"""
Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

# Inheritance

class Person:
    def __init__(self,name,pid,email):
        # object attributes
        self.name = name
        self.pid = pid
        self.email = email

    def __str__(self):
        print(f'Name: {self.name} PID: {self.pid} Email: {self.email}')

    def introduce(self):
        print(f'My name is {self.name} I am Person.')


class Student(Person):
    def __init__(self,name,pid,email,sid,major):
        # method 1:
        #Person.__init__(self,name,pid,email)

        # method 2:
        super().__init__(name,pid,email)

        self.sid = sid
        self.major = major

    def __str__(self):
        print(f'Name: {self.name} PID: {self.pid} Email: {self.email} SID: {self.sid} Major: {self.major}')

    def introduce(self):
        print(f'My name is {self.name} I am Student.')


p1 = Person('SAM','001','sam@mail.com')
p1.__str__()

s1 = Student('Ton','002','ton@mail.com','s002','MIT')
s1.__str__()

p1.introduce()
s1.introduce()
