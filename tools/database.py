import os
import pickle  # for serialization

class UserDatabase:
    def __init__(self, file_path='database.pkl'):
        self.file_path = file_path
        self._users = self.load_users()

    def add_user(self, user):
        if not self.is_user_saved(user):
            self._users.append(user)
            self.save_users()
            print("Success")
        else:
            print("Username already exists in the database")

    def is_user_saved(self, user):
        return any(existing_user.username == user.username for existing_user in self._users)
    
    def get_users(self):
        return self._users

    def save_users(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self._users, file)

    def load_users(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as file:
                return pickle.load(file)
        return []

    def __str__(self):
        return "\n".join(str(user) for user in self._users)
