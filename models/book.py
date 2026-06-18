from utils.enums import BookStatus

class Book:
    book_count = 1
    status = BookStatus.AVAILABLE
    def __init__(self, title, author, isbn, copies):
        self.__book_id_counter =  Book.book_id_counter
        Book.book_count +=1
        self.__title = title
        self.__author = author
        self.isbn = isbn
        self.__copies = copies
        self.isBorrowed = False
        self.isReturned = False 
    #getters and setters for isbn
    @property
    def copies(self):
        return self.__copies
    @copies.setter
    def copies(self, value):
        if value.isdigit():
            self.__copies = int(value)
        else:
            print("Please enter a correct vlaue for the copies field")
    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, value):
        if (len(value) == 2 or len(value) == 10) and value.isdigit():
            self.__isbn = value
        else:
            print("Please enter a correct vlaue for the isbn field")
    def get_books_count(cls):
        """ Function needs for createing report.txt file """
        return cls.books_count
    @classmethod
    def get_book_info(cls):
        title = input("Enter a book name: ")
        author = input("Enter an author of the book:")
        isbn = input("Enter an isbn: ")
        copies = input("The count of the copies: ")
        return cls(title, author, isbn, copies)
    def create_single_book(self):
        tmp = {}
        tmp["id"] = self.__book_id_counter
        tmp["title"] = self.__title
        tmp["author"] = self.__author
        tmp["isbn"] = self.__isbn
        tmp["status"] = Book.status.name
        tmp["copies"] = self.__copies
        return tmp
    def __str__(self):
        return (
            f"Title: {self.__title}\n"
            f"Author: {self.__author}\n"
            f"ISBN: {self.__isbn}\n"
            f"Status: {Book.status.name}\n"
            f"Copies: {self.__copies}"
        )