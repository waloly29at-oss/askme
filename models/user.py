class User:
    def __init__(self, user_id, username, password, name, email, allow_anonymous):
        self.user_id = user_id        
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.allow_anonymous = allow_anonymous  