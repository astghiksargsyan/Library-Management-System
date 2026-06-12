from models.book import Book
from models.user import User
import json
from utils.books_functions import load_data
from utils.users_functions import login_function

from utils.enums import BookStatus
BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
class LibraryService:
    
    @staticmethod
    def borrow_book(books, users):
        print("First Login to borrow book")
        current_user = login_function()             
        if current_user:
            book_input = input("Enter book name or isbn: ")
            for book in books:
                if book_input == book["title"] or book_input == book["isbn"]:
                    book["status"] = BookStatus.BORROWED.name
                    with open(BOOKS_FILE, "w") as f:
                        json.dump(books, f, indent=4)
                    print("Successfully borrowed!")
                    current_user["borrowedbook"].append(book)
                    users.append(current_user)
                    with open(USERS_FILE, "w") as f:
                        json.dump(users, f, indent=4)  

                    return 
        print("Book not found")
    @staticmethod
    def append_to_borrowed_books(users):
        pass
            


        