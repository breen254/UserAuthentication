import bcrypt
from user_management import is_email_valid, database

def login(email, entered_password):
    for user in database.get_users():
        if user.email == email:
            if bcrypt.checkpw(entered_password.encode('utf-8'), user.password):
                print("Login successful!")
                return True
            else:
                print("Incorrect password. Please try again.")
                return False
    print("User not found. Please try again.")
    return False

if __name__ == "__main__":
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    if is_email_valid(email_input):
        login(email_input, password_input)
    else:
        print("Invalid email format. Please enter a valid email.")
