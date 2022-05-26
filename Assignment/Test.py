"""
Student Name: Supinya Sricharoen
ID: 364211760028
Grop: MIT211
"""

from Vehicle import Vehicle

Vehicle_store = []
num = int(input('คุณมีรถกี่คัน :'))

for x in range(num):
    brandname = input('ยี่ห้อรถ:')
    model = input('รุ่นรถ:')
    color = input('สีรถ:')
    max_speed = input('ความรเร็วสูงสุด:')
    price = float(input('ราคา:'))

    a = Vehicle(brandname,model,color,max_speed,price)
    Vehicle_store.append(a)

def display_Vehicle(Vehicle):
    print('จำนวนรถทั้งหมด:',len(Vehicle))
    for x in Vehicle:
        x.Vehicle_detail()

display_Vehicle(Vehicle_store)
