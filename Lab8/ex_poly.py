
from multipledispatch import dispatch

# polymorpshime

mylist = [1, 2, 3, 4, 5]
msg = 'Hello, OOP'
dict = {'name':'Ice','age':22,'major':'MIT'}

print(len(mylist))
print(len(msg))
print(len(dict))

@dispatch(str)
def introduce(name):
    print(f'My name is {name}')

@dispatch(str,int)
def introduce(name,age):
    print(f'My name is {name},I am {age} year old.')

introduce('ICE')
introduce('Ton',37)
