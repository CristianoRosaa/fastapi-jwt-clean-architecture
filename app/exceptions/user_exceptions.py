class UserNotFoundException(Exception):
    
    def __init__(self):
        self.message = "User not found"
        super(). __init__(self.message)


class InvalidCredentialsException(Exception):
    
    def  __init__(self):
        self.message = "Invalid Credentials"
        super().__init__(self.message)

class UsernameAlreadyExistsException(Exception):
    
    def __init__(self):
        self.message = "Username already exists"
        super().__init__(self.message)

class EmailAlreadyExistsException(Exception):

    def __init__(self):
        self.message = "Email already exists"
        super().__init__(self.message)