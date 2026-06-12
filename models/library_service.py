from models.book import Book
from models.user import User
import json
from utils.books_functions import load_data

from utils.enums import BookStatus
BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
class LibraryService:
    @staticmethod
    def borrow_book(books):
        book_input = input("Enter book name or isbn: ")
        for book in books:
            if book_input == book["title"] or book_input == book["isbn"]:
                book["status"] = BookStatus.BORROWED.name
                with open(BOOKS_FILE, "w") as f:
                    json.dump(books, f, indent=4)
                print("Successfully borrowed!")
                return 
        print("Book not found")
        