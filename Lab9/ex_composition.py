"""
Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

class Department:
    d_name = ''

class University:
    u_name = ''
    list_of_dapartment = list()

    def get_department(self):

        d1 = Department()
        d1.d_name = 'MT'
        d2 = Department()
        d2.d_name = 'Sci'

        self.list_of_dapartment.append(d1)
        self.list_of_dapartment.append(d2)

    def __str__(self):
        print(f'Department in {self.u_name}: ')
        for x in self.list_of_dapartment:
            print(x.d_name)


u1 = University()
u1.u_name = 'RUTS'
u1.get_department()
u1.__str__()