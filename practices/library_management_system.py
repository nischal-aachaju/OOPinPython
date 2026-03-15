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
            return "available"
        
        else:
            return "not available"
    
    def __str__(self):
        
        return f"{self.title} by {self.author} which is {self.is_available()} "
b1=Book("Munamodhan","laxmi persad devkota",1232)
b1.borrow()
print(b1.is_available())
print(b1)