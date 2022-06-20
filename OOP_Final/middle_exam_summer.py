"""
Student Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

class Student():
    def __init__(self, name, id, age, weigth, height):
        # object attributes
        self.__name = name
        self.__id = id
        self.__age = age
        self.__weigth = weigth
        self.__heigth = height

    # getter and setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_weight(self):
        return self.__weigth

    def set_weight(self, weigth):
        self.__weigth = weigth

    def get_heigth(self):
        return self.__heigth

    def set_hegith(self, heigth):
        self.__heigth = heigth

    def student_detail(self):
        print(f'\tSTD Name: {self.__name}\n'
                  f'\tID: {self.__id}\n'
                  f'\tAge: {self.__age}\n'
                  f'\tWeight: {self.__weigth}\n'
                  f'\tHeight: {self.__heigth}\n')


class Vaccine():
    def __init__(self,vac_name):
        self.__vac_name = vac_name

    #getter and setter method
    def get_vaccine(self):
        return self.__vac_name
    def set_vaccine(self,new_name):
        self.__vac_name = new_name

    def vaccine_detail(self):
        print(f'Vaccine name: {self.__vac_name}')

class Vaccinated():
    def __init__(self, student):
        self.student = student
        self.vaccinated = list() # []
        self.date = list() # []
    def add_vaccinated(self,vaccine):
        self.vaccinated.append(vaccine)
    def add_date(self,date):
        self.date.append(date)

    def vaccinated_detail(self):
        print('Student Vaccinated Informations:')
        self.student.student_detail()

        for i in range(len(self.vaccinated)):
            print(f'\tvaccine {i+1}: {self.vaccinated[i].get_vaccine()} date: {self.date[i]}')

"""
input name,id,age,weight,height ?
input How many vaccinated ? 
select vaccines
input date(str)
"""

name = input('Student Name?: ')
id = input('Student ID?: ')
age = int(input('Age?: '))
weigth = float(input('Weigth? (kg): '))
heigth = float(input('Heigth? (cm): '))

num = int(input('How many your vaccinated ? : '))
vacc = list()
date = list()
select = 1

for x in range(num):
    if age >= 18:
      print()
    else:
      exit("อายุคุณยังไม่ถึง 18 ปี")
    print(f'which vaccine {x+1}:')
    print("\t1.sinovac")
    print('\t2.astrazeneca')
    print('\t3.johnson&johnson')
    print('\t4.moderna')
    print('\t5.sinopharm')
    print('\t6.pfizer')
    while True:
        select = int(input('select(1-6): '))
        if select >=1 and select <=6:
            break
        print('Please, enter number 1-6 only.')

    if select == 1:
        vacc.append('sinovac')
    elif select == 2:
        vacc.append('astrazeneca')
    elif select == 3:
        vacc.append('johnson&johnson')
    elif select == 4:
        vacc.append('moderna')
    elif select == 5:
        vacc.append('sinopharm')
    elif select == 6:
        vacc.append('pfizer')
    else:
        print('Please, enter number 1-6 only.')

    d = input('Date: ')
    date.append(d)

# add data to object
std = Student(name, id, age, weigth, heigth)
v = []
# list of vaccine object
for x in vacc:
    v.append(Vaccine(x))

std_vac = Vaccinated(std)
for x in v:
    std_vac.add_vaccinated(x)
for x in date:
    std_vac.add_date(x)

std_vac.vaccinated_detail()


# print([x for x in vacc])
# print([x for x in date])

