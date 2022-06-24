"""
Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

class Person:
    def __init__(self,name,email,tel):
        # object attributes
        self.__name = name  # private member
        self.__email = email
        self.__tel = tel

# getter and setter method
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_email(self):
        return self.__email
    def set_email(self, new_email):
        self.__email = new_email
    def get_tel(self):
        return self.__tel
    def set_tel(self, new_tel):
        self.__tel = new_tel

# display Person object
    def __str__(self):
        print(f'\tName: {self.__name}\n'
                  f'\tEmail: {self.__email}\n'
                  f'\tTel: {self.__tel}\n')

class Student(Person):
    def __init__(self,name,email,tel,sid,major):
        super().__init__(name,email,tel)
        #Person.__init__(self,name,email,tel)
        self.__sid = sid
        self.__major = major

    # getter and setter
    def get_id(self):
        return  self.__sid
    def set_id(self, new_sid):
        self.__sid = new_sid
    def get_major(self):
        return  self.__major
    def set_major(self, new_major):
        self.__major = new_major

    def __str__(self):
        print(' ')
        super().__str__()
        print(f'\tSID: {self.__sid}\n'
              f'\tMajor: {self.__major}\n')

class Employee(Person):
    def __init__(self,name,email,tel,eid,position):
        super().__init__(name,email,tel)
        self.__eid = eid
        self.__position = position

    def get_eid(self):
        return self.__eid
    def set_eid(self,new_eid):
        self.__eid = new_eid
    def get_position(self):
        return self.__position
    def set_position(self,new_position):
        self.__position = new_position

    def __str__(self):
        print(' ')
        super().__str__()
        print(f'\tEid: {self.__eid}\n')
        print(f'\tPosition: {self.__position}\n')

class Courses():

    all_courses = ['Digital Marketing for Small Business',
                   'Accounting for SME', 'Chatbot for E-Commerce',
                   'Data Analytics for Small Business']

    def __init__(self,courses_id,courses_name):
        self.__courses_id = courses_id
        self.__courses_name = courses_name

    #getter and setter method
    def get_courses01(self):
        return self.__courses_id
    def set_courses01(self,new_id):
        self.__courses_id = new_id
    def get_courses(self):
        return self.__courses_name
    def set_courses(self,new_name):
        self.__courses_name = new_name

    def __str__(self):
        print(f'ID: {self.__courses_id}')
        print(f'Courses name: {self.__courses_name}')

class CourseRegistration():
    def __init__(self, id):
        self.id = id
        self.course_regis = list()

    def add_course(self,course):
        self.course = course

    def __str__(self):
        self.id.__str__()
        for x in self.course:
            print(f'\tcourse {self.course.index(x)+1}: {x[0].get_course()}  \t\tdate: {x[1]}')