"""
Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

class Department:
    d_name = ''
    list_of_teacher = list()

    def __str__(self):
        print(f'list of Teachers: ')
        for x in self.list_of_teacher:
            print(x.t_name)

class Teacher:
    t_name = ''

t1 = Teacher()
t1.t_name = 'Supinya'
t2 = Teacher()
t2.t_name = 'Piyapong'

d1 = Department()
d1.d_name = 'Management Technology'

d1.list_of_teacher = [t1,t2]

print(d1.d_name,'and here is list of teacher: ')
for x in d1.list_of_teacher:
    print(x.t_name)

d1.list_of_teacher.pop()

d1.__str__()