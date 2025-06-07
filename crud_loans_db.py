import datetime
from database.models import Book, Loan
from db_connector import *

def query_active_loans_db():
    try:
        session = connect_db()
        loans = session.query(Loan).filter(Loan.return_date == None).all()
        return loans
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def query_active_loans_by_user_db(user_id, book_id=False):
    try:
        session = connect_db()
        filters = [Loan.user_id == user_id, Loan.return_date == None]
        if book_id:
            filters.append(Loan.book_id == book_id)
        loans = session.query(Loan).filter(*filters).all()
        return loans
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def query_closed_loans_db():
    try:
        session = connect_db()
        loans = session.query(Loan).filter(Loan.return_date != None).all()
        return loans
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def create_loan_db(book_id, user_id):
    try:
        session = connect_db()
        loan = Loan(book_id=book_id, user_id=user_id, loan_date=datetime.datetime.now(), return_date=None)
        session.add(loan)
        book = session.query(Book).filter_by(id=book_id).first()
        book.availability -= 1
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)
        
def create_return_db(book_id):
    try:
        session = connect_db()
        loan = session.query(Loan).filter(Loan.book_id == book_id, Loan.return_date == None).first()
        loan.return_date = datetime.datetime.now()
        book = session.query(Book).filter_by(id=book_id).first()
        book.availability += 1
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)