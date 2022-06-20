"""
Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

from model import Student,Vaccine,VaccinatedPassport,Employee

def display_vaccine():
    n = 1
    for x in Vaccine.all_vaccine:
        print(f'\t{n}. {x} ')
        n += 1

def validate_age(a):
    if a >= 18:
        return True
    else:
        return False

def input_person():
    name = input('Name: ')

    while True:
        age = int(input('Age: '))
        if validate_age(age):
            break
        else:
            print('Age should be higher than 18 year old.')

    weight = float(input('Weight (kg): '))
    height = float(input('Height (cm): '))

    return name,age,weight,height

def input_student():
    id = input('Student ID: ')
    major = input('Major: ')
    return id,major

def input_employee():
    position = input('Position: ')
    return position

def input_vaccine():
    num = int(input('How many your vaccinated ? : '))

    vaccinate_date = list()

    for x in range(num):
        display_vaccine()
        n = len(Vaccine.all_vaccine)
        while True:
            select = int(input(f'select(1-{n}): '))
            if select >= 1 and select <= n:
                break
            print(f'Please, enter number 1-{n} only.')

        d = input('Date: ')

        vaccinate_date.append([Vaccine(Vaccine.all_vaccine[select - 1]), d])

    return vaccinate_date


if __name__ == '__main__':
    print('Enter your information: ')
    p = input_person()

    x = input('Are you Student(s) or Employee(e) :: (s/e): ?')
    if x.lower() == 's':
        s = input_student()
        s = Student(p[0], p[1], p[2], p[3], s[0], s[1])
    else:
        position = input_employee()
        s = Employee(p[0], p[1], p[2], p[3],position)

    v_s = VaccinatedPassport(s)
    v_s.add_vaccinated(input_vaccine())

    v_s.__str__()


