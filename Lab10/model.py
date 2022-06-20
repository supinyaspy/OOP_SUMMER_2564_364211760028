"""
Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

class Person:
    def __init__(self,name,age,weight,height):
        # object attributes
        self.__name = name # private member
        self.__age = age
        self.__weight = weight
        self.__height = height

    # getter and setter method
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight
    def get_height(self):
        return self.__height
    def set_hegiht(self, height):
        self.__height = height

    # display Person object
    def __str__(self):
        print(f'\tName: {self.__name}\n'
                  f'\tAge: {self.__age}\n'
                  f'\tWeight: {self.__weight}\n'
                  f'\tHeight: {self.__height}\n')

class Student(Person):
    def __init__(self,name,age,weight,height,id,major):
        super().__init__(name,age,weight,height)
        #Person.__init__(self,name,age,weight,height)
        self.__id = id
        self.__major = major

    # getter and setter
    def get_id(self):
        return  self.__id
    def set_id(self,id):
        self.__id = id
    def get_major(self):
        return  self.__major
    def set_major(self,major):
        self.__major = major

    def __str__(self):
        super().__str__()
        print(f'\tSID: {self.__id}\n'
              f'\tMajor: {self.__major}\n')

class Vaccine():

    all_vaccine = ['Sinovac', 'Astrazeneca', 'Johnson&Johnson', 'Moderna', 'Sinopharm', 'Pfizer']

    def __init__(self,vac_name):
        self.__vac_name = vac_name

    #getter and setter method
    def get_vaccine(self):
        return self.__vac_name
    def set_vaccine(self,new_name):
        self.__vac_name = new_name

    def __str__(self):
        print(f'Vaccine name: {self.__vac_name}')

class VaccinatedPassport():
    def __init__(self, owner):
        self.owner = owner
        self.vaccinated = list() # [] ==> [[v1,'11/7/2564'],[v2,10/10/2564]]

    def add_vaccinated(self,vaccine):
        self.vaccinated = vaccine

    def __str__(self):
        print('MT Vaccinated Passport :')
        self.owner.__str__()
        for x in self.vaccinated:
            print(f'\tvaccine {self.vaccinated.index(x)+1}: {x[0].get_vaccine()}  \t\tdate: {x[1]}')


class Employee(Person):
    def __init__(self,name,age,weight,height,position):
        super().__init__(name,age,weight,height)
        self.__position = position

    def get_position(self):
        return self.__position
    def set_position(self,position):
        self.__position = position

    def __str__(self):
        super().__str__()
        print(f'\tPosition: {self.__position}\n')
