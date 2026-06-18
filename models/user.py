import uuid

class User:
    def __init__(self, name, username, password):
        self.id = str(uuid.uuid4())
        self.__name = name
        self.__username = username
        self.__password = password
        self.borrowedbook = []
        self.history = []
    @classmethod
    def get_user_info_register(cls):
        """Collect user information from user input."""
        username = input("Enter a username: ")
        name = input("Enter a name: ")
        password = input("Set a password: ")
        return cls(name, username, password)
    def create_user(self):
        """Create a dictionary representation of the user for JSON storage."""
        tmp = {}
        tmp["user_id"] = self.id 
        tmp["username"] = self.__username
        tmp["name"] = self.__name
        tmp["password"] = self.__password
        tmp["borrowedbook"] = self.borrowedbook
        tmp["history"] = self.history
        return tmp
    @property
    def username(self):
        """Return the username."""
        return self.__username
    def __str__(self):  
        """Return a readable string representation of the user.""" 
        return (
            f"ID: {self.id}"
            f"Name: {self.__name}\n"
            f"Username: {self.__username}\n"
            f"The books borrowed by {self.__name}: {self.borrowedbook}\n"
        )
    
