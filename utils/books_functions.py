import json
from models.book import Book
from utils.enums import BookStatus
DATA_FILE = "data/books.json"

def load_data():
    """Load the book list from the file"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
            
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)
def save_data(book):
    """Add single book into the book list"""
    books = load_data()
    books.append(book.create_single_book())
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)
    print("Successfully added!")
def display_books():
    """Function for displaying all available books"""
    print("All avialable books:")
    print("#"*20)
    books = load_data()
    for book in books:
        print("Book info:")
        print(f"The title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"isbn: {book['isbn']}")
        print(f"Status: {book['status']}")
        print(f"Number of copies: {book['copies']}")
        print("*" * 20)

def search_by_author_function():
    user_input_for_author = input("Enter book author: ")
    books = load_data()
    found = False
    for book in books:
        if book['author'].lower() == user_input_for_author.lower():
            print("Book info:")
            print(f"The title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"isbn: {book['isbn']}")
            print(f"Status: {book['status']}")
            print(f"Number of copies: {book['copies']}")
            print("*" * 20)
            found = True
    if not found:
        print("Nothing Found")

def search_by_book_name_function():
    user_input_book_name = input("Enter book name: ").lower()
    books = load_data()
    found = False
    for book in books:
        if book['name'].lower() == user_input_book_name:
            print("Book info:")
            print(f"The title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"isbn: {book['isbn']}")
            print(f"Status: {book['status']}")
            print(f"Number of copies: {book['copies']}")
            print("*" * 20)
            found = True
    if not found:
        print("Nothing Found")
def add_book():
    book = Book.get_book_info()
    save_data(book)