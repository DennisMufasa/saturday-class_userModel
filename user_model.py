import re
database = []   # liist to store user details

class User:
    """A class that manipulates user details"""
    def __init__(self, first_name, last_name, email, password):
        """User class constructor"""
        self.first_name = first_name
        self.last_name  = last_name
        self.email = email
        self.password = password
    def save_user(self):
        """A method to save a new user"""
        # check if the email has an @ symbol
        if bool(re.search(r'@', self.email)) is False:
            print("Ensure your email has an @ symbol")
            return "Try again"
        # check length of password to ensure it between 6 and 12 chars
        if len(self.password) < 6 or len(self.password) > 12:
            print("Make sure your password is between 6 and 12 characters")
            return "Try again"
        # create a dictionary to represent a single user
        user = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }
        # save a new user in our database
        database.append(user)
        print("New user saved!")
