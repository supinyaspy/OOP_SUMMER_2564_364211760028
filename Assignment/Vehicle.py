"""
Student Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""
class Vehicle:
    def __init__(self,brandname,model,color,max_speed,price):
        # object attributes
        self.brandname = brandname
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price

    def Vehicle_detail(self):
        print(f'brandname:{self.brandname} model: {self.model} '
              f'color:{self.color} max_speed:{self.max_speed} price: {self.price}  THB')