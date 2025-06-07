from utils import *
from crud_users_db import *

def list_users():
    print("\n--- Users ---")
    users = query_users_db()
    if not users:
        print("! No users registered !")
        return
    for u in users:
        print(f"{u.id} - {u.first_name} {u.last_name}")

def create_user():
    print("\n--- Register user ---")
    first_name = input("Enter the first name: ").strip()
    last_name = input("Enter the last name: ").strip()
    birth_date = insert_birth_date("Enter the birth date (dd-mm-yyyy): ")
    if birth_date:
        create_user_db(first_name, last_name, birth_date)
        print(">> User registered successfully!")

def delete_user():
    print("\n--- Delete User ---")
    list_users()
    
    user_id = insert_user_id("Enter the ID of the user you want to delete: ")
    if user_id is None:
        return
        
    user = query_user_db(user_id)

    if not user:
        print("! User not found !")
        return

    confirmation = input(f"Are you sure you want to delete the user {user.first_name} {user.last_name}? (y/n): ").strip().lower()
    if confirmation != "y":
        print(">> Operation cancelled.")
        return

    delete_user_db(user)
    print(">> User deleted successfully!")