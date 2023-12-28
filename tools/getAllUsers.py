from user_management import database

for users in database.get_users():
    print(users)
