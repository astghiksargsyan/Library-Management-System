import json
from models.user import User
DATA_FILE_USERS = "data/users.json"

def load_users_data():
    """Load the users from the file"""
    try:
        with open(DATA_FILE_USERS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_user(users, user):
    """Add a registered user to the JSON file."""
    users.append(user.create_user())
    with open(DATA_FILE_USERS, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
    print("Successfully added!")
def login_function():
    """username and password validation"""
    username = input("Enter a username: ")
    password = input("Set a password: ")
    users = load_users_data()
    for user in users:
        if username == user["username"] and password == user["password"]:
            print("Successfully logged in")
            return user
    print("Wrong login information")
    return None

def view_account():
    """View account information"""
    print("To view your account, you should first log in:: ")
    current_user = login_function()
    if current_user:
        print("Account details:")
        print (
            f"ID: {current_user["user_id"]}"
            f"Name:{current_user["name"]}\n"
            f"Username: {current_user["username"]}\n"
            f"The books borrowed by {current_user["name"]}: {current_user["borrowedbook"]}\n"
        )
    else:
        print("Access denied.")
def check_username(username):
    """Check if a username already exists."""
    users = load_users_data()
    for user in users:
        if user["username"] == username:
            return True
    return False
    
def add_user():
    """Create a new user and save it to the JSON file."""
    users = load_users_data()
    user = User.get_user_info_register()
    if check_username(user.username):
        print("Username already exists. Choose another!")
        return
    save_user(users, user)