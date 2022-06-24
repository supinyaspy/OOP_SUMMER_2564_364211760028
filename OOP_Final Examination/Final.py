"""
Student Name: Supinya Sricharoen
ID: 364211760028
Grop: MIT211
"""
from Final2 import Person,Student,Employee,Courses,CourseRegistration
display_Courses():
    n = 1
    for x in Courses.all_courses:
        print(f'\t{n}. {x} ')
        n += 1

def input_person():
    name = input('Name: ')

    email = input(input('Email: '))
    tel = float(input('Tel : '))

    return name,email,tel

def input_student():
    id = input('Student ID: ')
    major = input('Major: ')
    return id,major

def input_employee():
    position = input('Position: ')
    return position

def input_courses():
    num = int(input('How many your Courses? : '))
    def validate_regis(a):
        if a <= 3:
            return True
        else:
            return False
        while True:
            regis = int(input('regis: '))
            if validate_regis(regis):
                break
            else:
                print('สามารถลงทะเบียนกิจกรรมได้มากกว่า 1 กิจกรรม แต่ไม่เกิน 3 กิจกรรม')

    course_date = list()

    for x in range(num):
        display_Courses()
        n = len(Courses.all_courses)
        while True:
            select = int(input(f'select(1-{n}): '))
            if select >= 1 and select <= n:
                break
            print(f'Please, enter number 1-{n} only.')

        course_date.append([Courses(Courses.all_courses[select - 1])])

    return course_date

if _name_ == '_main_':
    print('Enter your information: ')
    p = input_person()
    s = input_student()

    c_s = CourseRegistration(s)
    c_s.add_course(input_courses())
    c_s.__str__()