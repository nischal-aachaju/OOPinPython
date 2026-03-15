class Book:
    
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.__is_borrowed=False

    def borrow(self):
        self.__is_borrowed=True
        return self.__is_borrowed
    
    def return_book(self):
        self.__is_borrowed=False
        return self.__is_borrowed

    def is_available(self):
        if not self.__is_borrowed:
            return True
        
        else:
            return False
    
    def __str__(self):
        self.is_book_available="available" if self.is_available() else "not available"
        return f"{self.title} by {self.author} which is {self.is_book_available} "

class Member:
    
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.__borrowed_books=[]

    def borrow_book(self,book):
        
        if book.is_available():
            self.__borrowed_books.append(book)
            book.borrow()
            print(f"{book.title} is successfully Booked by {self.name}")
        else:
            print(f"{book.title} is already Booked")
    
    def return_book(self,book):
        book.return_book()
        self.__borrowed_books.remove(book)
        print(f"{book.title} is returned by {self.name}")
    
    def get_borrowed_books(self):
        return f"{[book.title for book in self.__borrowed_books] if self.__borrowed_books else "no books"}"
    def __str__(self):
        return f"{self.name} borrowed {[book.title for book in self.__borrowed_books] if self.__borrowed_books else "no books"}"

# b1=Book("Muna Madan", "Laxmi parshad Devokta",121)
# b2=Book("Shiris Ko Phool","Parijat",111)
# print(b1)
# print(b2)
# m1=Member("Nischal",121)
# print(m1)
# m1.borrow_book(b1)
# m1.borrow_book(b2)
# print(m1.get_borrowed_books())
# print(b1)
# print(b2)
# m1.return_book(b1)
# print(m1.get_borrowed_book())
# print(b1)
# print(b2)