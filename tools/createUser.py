from user_management import create_user, is_email_unique, is_email_valid, is_valid_password

while True:
    try:
        username = input("Input username: ")
        email = input("Input email: ")
        password = input("Input password: ")

        # Check if the email already exists in the database
        if not is_email_unique(email):
            raise ValueError("Email is already in use")

        # Check if the email has a valid format
        if not is_email_valid(email):
            raise ValueError("Invalid email format i.e example@example.com")
        
        if not is_valid_password(password):
            raise ValueError("Wrong password format. The password MUST have 8 characters long, special characters ie @#$%^&*,. and a number")

        # Create the user if both checks pass
        create_user(username, email, password)
        break  # Break out of the loop if the user input is valid

    except ValueError as e:
        print(f"Error: {e}")


