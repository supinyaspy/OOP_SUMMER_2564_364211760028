

class Ractangle():
    def __init__(self,w,l):
        # object attributes
        self.width = w
        self.length = l
    # def cal_area(self,x,y):
    #     print('Area of rectangle is: ', (x*y))
    def cal_area(self):
        print('Area of rectangle is: ', (self.width*self.length))

class Triangle():
    def __init__(self,b,h):
        # object attributes
        self.base = b
        self.high = h
    # def cal_area(self,b,h):
    #     print('Area of triangle is: ',(0.5*b*h))
    def cal_area(self):
        print('Area of triangle is: ',(0.5*self.base*self.high))


def calArea(obj,a,b):
    obj.cal_area(a,b)

r = Ractangle(5,10)
t = Triangle(10,20)
# solution 1
# r.cal_area(5,10)
# t.cal_area(10,20)

# solution 2
# calArea(r,5,10)
# calArea(t,10,20)

# solution 3
for obj in (r,t):
    obj.cal_area()