# user_management.py
import uuid
import re
import bcrypt
from user import User
from database import UserDatabase

def generate_uid():
    return str(uuid.uuid4())

def is_valid_password(password):
    # Password should be 8 characters long, contain at least one digit, and have at least one of @#$%,.*&
    password_pattern = re.compile(r'^(?=.*[0-9])(?=.*[@#$%,.*&])[A-Za-z0-9@#$%,.*&]{8,}$')
    return bool(re.match(password_pattern, password))

def is_email_valid(email):
    # Regular expression for a basic email format check
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))

def is_email_unique(email):
    return all(existing_user.email != email for existing_user in database.get_users())

def hash_password(password):
    # Hash the password using bcrypt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def create_user(username, email, password):
    if email != "" and password != "":
        if is_email_valid(email):
            if is_email_unique(email):
                if is_valid_password(password):
                    uid = generate_uid()
                    hashed_password = hash_password(password)
                    user_created = User(uid, username, email, hashed_password)
                    database.add_user(user_created)
                else:
                    raise ValueError("Invalid password format")
            else:
                raise ValueError("Email is already in use")
        else:
            raise ValueError("Invalid email format")
    else:
        raise ValueError("Email and password cannot be empty")



database = UserDatabase()

