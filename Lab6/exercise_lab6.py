"""
Student Name: {Supinya Sricharoen}
ID: {364211760028}
Grop: {MIT211}
"""

"""
จงเขียนโปรแกรมรับค่าข้อมูลหนังสือ ประกอบด้ย ชื่อหนังสือ ราคา ผู้แต่ง สำนักพิมพ์
โดยการถามผู้ใช้ว่า มีหนังสือกี่เล่ม จากนั้นให้รับค่าข้อมูลดังกล่าว และเก็บข้อมูลไว้ใน object จากนั้นเก็บ
object ไว้ใน list ชื่อ mybook_store แสดงผลข้อมูลทั้งหมดทางหน้าจอภาพ

ัตัวอย่างนำเข้าข้อมูล เช่น
คุณมีหนังสือท้ังหมดกี่เล่ม: 1 
ชื่อหนังสือ: OOP
ราคา: 200
ผู้แต่ง: ภูริวัฒน์ เลิศไกร
สำนักพิมพ์: MT

ตัวอย่างแสดงผล เช่น
Book name: OOP | Price: 200.0 THB | Auther: Puriwat Lertkrai | Publisher: MT Familly
"""


from book import Book

book_store = []
num = int(input('คุณมีหนังสือทั้งหมดกี่เล่ม? :'))

for x in range(num):
    bookname = input('ชื่อหนังสือ:')
    price = float(input('ราคา:'))
    auther = input('ชื่อผู้แต่ง:')
    publisher = input('สำนักพิมพ์:')
    #1
    b = Book(bookname,price,auther,publisher)
    book_store.append(b)
    #2
    #book_store.append(Book(bookname,price,auther,publisher))

def display_book(book):
    print('จำนวนหนังสือทั้งหมด:',len(book))
    for x in book:
        x.book_detail()

display_book(book_store)




