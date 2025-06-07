from database.models import Book
from db_connector import *

def list_books_db():
    try:
        session = connect_db()
        books = session.query(Book).all()
        return books
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def query_book_db(book_id):
    try:
        session = connect_db()
        book = session.query(Book).filter_by(id=book_id).first()
        return book
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)