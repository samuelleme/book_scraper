from crud_books_db import *

def list_books():
    print("\n--- Books ---")
    books = list_books_db()
    if not books:
        print("! No books registered !")
        return
    for b in books:
        print(f"{b.id} - {b.title} | Availability: {b.availability}")