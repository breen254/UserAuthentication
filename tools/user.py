class User:
    def __init__(self, uid, username, email, password):
        self.uid = uid
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"Username: {self.username} email: {self.email}"


