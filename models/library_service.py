from models.book import Book
from models.user import User
import json
from utils.books_functions import load_data
from utils.users_functions import login_function
from utils.enums import BookStatus
BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
class LibraryService:
    def __init__(self, BOOKS_FILE, USERS_FILE):
        self.BOOKS_FILE = BOOKS_FILE
        self.USERS_FILE = USERS_FILE
    @staticmethod

    def return_book(books, users):
        print("First Login to return book")
        current_user = login_function()

        if current_user:
            book_input = input("Enter book name or isbn: ")
            for book in books:
                if book_input == book["title"] or book_input == book["isbn"]:
                    for borrowed_book in current_user["borrowedbook"]:
                        if borrowed_book["isbn"] == book["isbn"]:
                            current_user["borrowedbook"].remove(borrowed_book)
                            book["copies"] += 1
                            book["status"] = BookStatus.AVAILABLE.name
                            LibraryService.updat_books(books)
                            for user in users:
                                if user["username"] == current_user["username"]:
                                    user["borrowedbook"] = current_user["borrowedbook"]
                                    break
                            LibraryService.update_users(users)
                            print("Successfully returned!")
                            return
        print("Book not found or not borrowed by this user.")
    @staticmethod
    def borrow_book(books, users):
        print("First Login to borrow book")
        current_user = login_function()             
        if current_user:
            book_input = input("Enter book name or isbn: ")
            for book in books:
                if (book_input == book["title"] or book_input == book["isbn"]) and LibraryService.check_book_availability(book):
                    book["status"] = BookStatus.BORROWED.name
                    book["copies"] -= 1  
                    LibraryService.updat_books(books)
                    print("Successfully borrowed!")
                    current_user["borrowedbook"].append(book)
                    for user in users:
                        if user["username"] == current_user["username"]:
                            user["borrowedbook"] = current_user["borrowedbook"]
                            break
                    LibraryService.update_users(users)
                    return 
    @staticmethod
    def update_users(users):
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4) 
    @staticmethod
    def updat_books(books):
        with open(BOOKS_FILE, "w") as f:
            json.dump(books, f, indent=4)
    @staticmethod
    def check_book_availability(book):
        return book["copies"] > 0 or book["status"] == BookStatus.AVAILABLE.name
                
        
    

            


        