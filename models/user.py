import uuid

class User:
    users_count = 0
    def __init__(self, name, username, password):
        self.id = str(uuid.uuid4())
        self.__name = name
        self.__username = username
        self.__password = password
        self.borrowedbook = []
        self.history = []
        User.users_count += 1
    @classmethod
    def get_user_info_register(cls):
        username = input("Enter a username: ")
        name = input("Enter a name: ")
        password = input("Set a password: ")
        return cls(name, username, password)
    def create_user(self):
        tmp = {}
        tmp["user_id"] = self.id 
        tmp["username"] = self.__username
        tmp["name"] = self.__name
        tmp["password"] = self.__password
        tmp["borrowedbook"] = self.borrowedbook
        tmp["history"] = self.history
        return tmp
    @classmethod
    def get_users_count(cls):
        """ Function needs for createing report.txt file """
        print("User_count form users",  cls.users_count)
        return cls.users_count
    def __str__(self):   
        return (
            f"ID: {self.id}"
            f"Name: {self.__name}\n"
            f"Username: {self.__username}\n"
            f"The books borrowed by {self.__name}: {self.borrowedbook}\n"
        )
    
