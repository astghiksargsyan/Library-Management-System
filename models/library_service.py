from models.book import Book
from models.user import User
import json
import datetime
from utils.books_functions import load_data
from utils.users_functions import login_function
from utils.enums import BookStatus
BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
class LibraryService:
    def __init__(self, BOOKS_FILE, USERS_FILE):
        self.BOOKS_FILE = BOOKS_FILE
        self.USERS_FILE = USERS_FILE
    @classmethod
    def count_total_books(cls):
        """Calculate and save the total number of books to the report."""
        with open(BOOKS_FILE, "r") as f:
            info = json.load(f)
        LibraryService.total_books = len(info)
        LibraryService.save_to_report_file(f"Total count of books: {LibraryService.total_books}")
    @classmethod
    def count_total_users(cls):
        """Calculate and save the total number of users to the report."""
        with open(USERS_FILE, "r") as f:
            info = json.load(f)
        LibraryService.total_members = len(info)
        LibraryService.save_to_report_file(f"Total count of members: {LibraryService.total_members}")
    @staticmethod
    def save_to_report_file(data):
        """Save statistics data to the report.txt file."""
        with open("report.txt", 'a') as f:
            f.write(str(datetime.datetime.now()))
            f.write(" Updated info in currnt time ")
            f.write(data + "\n")
    @staticmethod
    def return_book(books, users):
        """Return a borrowed book."""
        print("First Login to return book")
        current_user = login_function()
        if current_user:
            book_input = input("Enter book name or isbn: ")
            for book in books:
                if book_input == book["title"] or book_input == book["isbn"]:
                    for borrowed_book in current_user["borrowedbook"]:
                        if borrowed_book["isbn"] == book["isbn"]:
                            current_user["borrowedbook"].remove(borrowed_book)
                            current_user["history"].append(f"returned book: {book["title"]}")
                            book["copies"] += 1
                            LibraryService.updat_books(books)
                            for user in users:
                                if user["username"] == current_user["username"]:
                                    user["borrowedbook"] = current_user["borrowedbook"]
                                    user["history"] = current_user["history"]
                                    break
                            LibraryService.update_users(users)
                            print("Successfully returned!")
                            return
        print("Book not found or not borrowed by this user.")
    @staticmethod
    def borrow_book(books, users):
        """Borrow a book from the library."""
        print("First Login to borrow book")
        current_user = login_function()             
        if current_user:
            book_input = input("Enter book name or isbn: ")
            for book in books:
                if (book_input == book["title"] or book_input == book["isbn"]) and LibraryService.check_book_availability(book):
                    LibraryService.change_book_status()
                    book["copies"] -= 1  
                    LibraryService.updat_books(books)
                    print("Successfully borrowed!")
                    current_user["borrowedbook"].append(book)
                    current_user["history"].append(f"borrowed book: {book["title"]}")
                    for user in users:
                        if user["username"] == current_user["username"]:
                            user["borrowedbook"] = current_user["borrowedbook"]
                            user["history"] = current_user["history"]
                            break
                    LibraryService.update_users(users)
                    return 
    @staticmethod
    def update_users(users):
        """Update user information in the JSON file."""
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4) 
    @staticmethod
    def updat_books(books):
        """Update book information in the JSON file."""
        with open(BOOKS_FILE, "w") as f:
            json.dump(books, f, indent=4)
    @staticmethod
    def change_book_status(book):
        """Update the book status based on the number of available copies."""
        if book["copies"] <= 0:
            Book.status = BookStatus.BORROWED.name 

    @staticmethod
    def check_book_availability(book):
        """Check the status and the copies count"""
        return book["copies"] > 0 or book["status"] == BookStatus.AVAILABLE.name
                