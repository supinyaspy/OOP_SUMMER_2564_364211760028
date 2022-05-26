"""
Student Name: {}
ID: {}
Grop: {}
"""

"""
Example:
Book
attributes: book_name(str),price(float),auther(str),publisher(str)
"""

# create class
class Book:
    def __init__(self,bookname,price,auther,publisher):
        # object attributes
        self.bookname = bookname
        self.price = price
        self.auther = auther
        self.publisher = publisher
    def book_detail(self):
        print(f'Book name:{self.bookname} Price: {self.price} THB '
              f'Auther:{self.auther} Publisher:{self.publisher}')


# create object
# b1 = Book("oop",200.00,"Supinya Sricharoen","MT Familly")
# b2 = Book("Computer Programming",300.00,"Supinya Sricharoen","RUTS")
#
# # display object attribute
# # print(b1.bookname)
# # print(b1.price)
# # print(b1.auther)
# # print(b1.publisher)
# #
# # print(b2.bookname)
# # print(b2.price)
# # print(b2.auther)
# # print(b2.publisher)
# #
# # b2.price = 399.00
# # print(b2.price)
# # print(b1.price)
# b1.book_detail()
# b2.book_detail()
#
# mybook = [b1, b2]
# # print("Dispay book form list: ")
# # for x in mybook:
# #     print(x.book_detail())
#
# for x in mybook:
#     print(x.book_detail())
