"""
Student Name: Supinya Sricharoen
ID: 364211760028
Grop: MIT211
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

    def student_detail(self):  # def __str__
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
        self.vaccinated = list() # [] ==> [[v1,'11/7/2564'],[v2,10/10/2564]]

    def add_vaccinated(self,vaccine):
        self.vaccinated = vaccine

        # using dicitonary
        # {'vacc1':[v1,'11/7/2564'], 'vacc2':[,]}

    def vaccinated_detail(self):
        print('Student Vaccinated Informations :')
        self.student.student_detail()
        for x in self.vaccinated:
            print(f'\tvaccine {self.vaccinated.index(x)+1}: {x[0].get_vaccine()}  \t\tdate: {x[1]}')


"""
input name,id,age,weight,height ?
input How many vaccinated ? 
select vaccines
input date(str)
"""
all_vaccine = ['Sinovac','Astrazeneca','Johnson&Johnson','Moderna','Sinopharm','Pfizer']

def display_vaccine():
    n = 1
    for x in all_vaccine:
        print(f'\t{n}. {x} ')
        n += 1

def validate_age(a):
    if a >= 18:
        return True
    else:
        return False

def input_name():
    n = input('Student Name: ')
    return n

name = input('Student Name: ')
id = input('Student ID: ')

while True:
    age = int(input('Age: '))
    if validate_age(age):
        break
    else:
        print('Age should be higher than 18 year old, or your input is not integer.')

weigth = float(input('Weigth (kg): '))
heigth = float(input('Heigth (cm): '))

num = int(input('How many your vaccinated ? : '))

vaccinate_date = list()

for x in range(num):
    display_vaccine()
    while True:
        select = int(input('select(1-6): '))
        if select >=1 and select <=len(all_vaccine):
            break
        print(f'Please, enter number 1-{len(all_vaccine)} only.')

    d = input('Date: ')

    vaccinate_date.append([Vaccine(all_vaccine[select-1]),d])


# add data to object

# create object Student
std = Student(name,id,age,weigth,heigth)
# create object Vaccinated
std_vac = Vaccinated(std)
# add vaccine and date to object Vaccinated
std_vac.add_vaccinated(vaccinate_date)
# display information about student and vaccinated
std_vac.vaccinated_detail()