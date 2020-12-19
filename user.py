
class User():

    def __init__(self):
        self.username = ""
        self.session_key = ""
        self.is_macro = False
        self.macro_users = list[str]

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<{self.username}, session_key: {self.session_key}, is_macro: {self.is_macro}, macro_users: {self.macro_users}>"