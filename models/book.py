from utils.enums import BookStatus

class Book:
    status = BookStatus.AVAILABLE
    def __init__(self, title, author, isbn, copies):
        self.__title = title
        self.__author = author
        self.isbn = isbn
        self.__copies = copies
        self.isBorrowed = False
        self.isReturned = False 
    #getters and setters for isbn
    @property
    def copies(self):
        """Return the number of available copies."""
        return self.__copies
    @copies.setter
    def copies(self, value):
        """Validate and set the number of copies."""
        if value.isdigit():
            self.__copies = int(value)
        else:
            print("Please enter a correct value for the copies field")
    @property
    def isbn(self):
        """Return the number of available isbn."""
        return self.__isbn
    @isbn.setter
    def isbn(self, value):
        """Validate and set the ISBN.
        Using 2-digit ISBNs during development/testing.
        Change to (10, 13) for production later."""
        if (len(value) == 2 or len(value) == 10) and value.isdigit():
            self.__isbn = value
        else:
            print("Please enter a correct value for the isbn field")
    @classmethod
    def get_book_info(cls):
        """Collect book information from user input."""
        title = input("Enter a book name: ")
        author = input("Enter an author of the book:")
        isbn = input("Enter an isbn: ")
        copies = input("The count of the copies: ")
        return cls(title, author, isbn, copies)
    def create_single_book(self):
        """Create a dictionary representation of the book for JSON storage."""
        tmp = {}
        tmp["title"] = self.__title
        tmp["author"] = self.__author
        tmp["isbn"] = self.__isbn
        tmp["status"] = Book.status.name
        tmp["copies"] = self.__copies
        return tmp
    def __str__(self):
        """Return a readable string representation of the book."""
        return (
            f"Title: {self.__title}\n"
            f"Author: {self.__author}\n"
            f"ISBN: {self.__isbn}\n"
            f"Status: {Book.status.name}\n"
            f"Copies: {self.__copies}"
        )