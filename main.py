from menu import *
from crud_users import *
from crud_books import *
from crud_loans import *

def main_menu():
    while True:
        option = display_menu()

        if option == "1":
            list_books()
        elif option == "2":
            list_users()
        elif option == "3":
            list_active_loans()
        elif option == "4":
            list_closed_loans()
        elif option == "5":
            create_user()
        elif option == "6":
            delete_user()
        elif option == "7":
            create_loan()
        elif option == "8":
            create_return()
        elif option == "0":
            print(">> Exiting the program...")
            break
        else:
            print("! Invalid option. Please try again !")

if __name__ == "__main__":
    main_menu()