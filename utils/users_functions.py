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
def save_user(user):
    """Add registred user into file"""
    users = load_users_data()
    users.append(user.create_user())
    with open(DATA_FILE_USERS, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
    print("Successfully added!")
def login_function():
    username = input("Enter a username: ")
    password = input("Set a password: ")
    users = load_users_data()
    login_flag = False
    for user in users:
        if username == user["username"] and password == user["password"]:
            print("Sucessfully Loged in")
            return user
            login_flag = True
    if not login_flag:
        print("Wrong login info")
    return None
def view_account():
    print("To veiw account you should first log in: ")
    current_user = login_function()
    if current_user:
        print("Account details:")
        print (
            f"ID: {current_user["user_id"]}"
            f"Name:{current_user["name"]}\n"
            f"Username: {current_user["username"]}\n"
            f"The books borrowed by {current_user["name"]}: {current_user["borrowed_book"]}\n"
        )
    else:
        print("Access denied.")


def add_user():
    user = User.get_user_info_register()
    save_user(user)