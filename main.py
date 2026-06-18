from models.book import Book
from models.user import User
from models.library_service import LibraryService
from utils.books_functions import add_book
from utils.books_functions import display_books
from utils.books_functions import search_by_author_function
from utils.books_functions import search_by_book_name_function
from utils.books_functions import load_data
from utils.users_functions import add_user
from utils.users_functions import login_function
from utils.users_functions import view_account
from utils.users_functions import load_users_data

books = load_data()
users = load_users_data()

def return_book():
    LibraryService.return_book(books, users)
def borrow_book():
    LibraryService.borrow_book(books, users)

init_option = (
    ("1", "Load available books", display_books),
    ("2", "Add book", add_book),
    ("3", "Search by Author", search_by_author_function),
    ("4", "Search by Book Name", search_by_book_name_function),
    ("5", "View Account", view_account),
    ("6", "Borrow book", borrow_book),
    ("7", "Return book", return_book),
    ("8", "Log in", login_function),
    ("9", "Register", add_user)
)

def main():
    print("#"*20)
    print("Choose available option: ")
    for id, name, _ in init_option:
        print(f"{id}. {name}")
    start_option = input("Enter the 1,2,3,4,5,6,7,8,9: ")
    flag = False
    for num,_, funct in init_option:
        if start_option == num:
            funct()
            flag = True
    if not flag:
        print("Enter the valid option's value")
main()