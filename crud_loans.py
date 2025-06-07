from db_connector import *
from crud_users import list_users
from crud_users_db import query_user_db
from crud_books import list_books, query_book_db
from utils import *
from crud_loans_db import *

def list_active_loans():
    print("\n--- Active loans ---")
    loans = query_active_loans_db()
    if not loans:
        print("! No active loans !")
        return
    for e in loans:
        book = query_book_db(e.book_id)
        user = query_user_db(e.user_id)
        print(f"Book: {book.title} (ID: {e.book_id}) | User: {user.first_name} {user.last_name} (ID: {e.user_id}) | Loan Date: {e.loan_date}")

def list_closed_loans():
    print("\n--- Closed loans ---")
    loans = query_closed_loans_db()
    if not loans:
        print("! No closed loans !")
        return
    for e in loans:
        book = query_book_db(e.book_id)
        user = query_user_db(e.user_id)
        print(f"Book: {book.title} (ID: {e.book_id}) | User: {user.first_name} {user.last_name} (ID: {e.user_id}) | Loan Date: {e.loan_date} | Return Date: {e.return_date}")

def create_loan():
    print("\n--- Create loan ---")
    list_users()
    user_id = insert_user_id("Enter the user ID: ")
    user = query_user_db(user_id)
    if not user:
        print("! User not found !")
        return

    loans = query_active_loans_by_user_db(user_id)
    if len(loans) >= 5:
        print("! This user already has 5 active loans !")
        return
    
    list_books()
    book_id = insert_book_id("Enter the book ID: ")
    book = query_book_db(book_id)
    if not book:
        print("! Book not found !")
        return
    if book.availability <= 0:
        print("! Book unavailable for loan !")
        return

    create_loan_db(book_id, user_id)
    print(">> Loan created successfully.")

def create_return():
    print("\n--- Create Return ---")
    list_users()
    user_id = insert_user_id("Enter the user ID: ")
    user = query_user_db(user_id)
    if not user:
        print("! User not found !")
        return

    loans = query_active_loans_by_user_db(user_id)
    if not loans:
        print("! No active loans for this user !")
        return

    print("Active loans:")
    for e in loans:
        book = query_book_db(e.book_id)
        print(f"Book: {book.title} (ID: {e.book_id}) | Loan Date: {e.loan_date}")

    book_id = insert_book_id("Enter the ID of the book to be returned: ")
    loan = query_active_loans_by_user_db(user_id, book_id=book_id)
    if not loan:
        print("! Loan not found for this user and book !")
        return

    create_return_db(book_id)
    print(">> Return created successfully.")