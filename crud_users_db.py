from database.models import User, Loan
from db_connector import *
from crud_loans_db import create_return_db

def create_user_db(first_name, last_name, birth_date):
    try:
        session = connect_db()
        new_user = User(first_name=first_name, last_name=last_name, birth_date=birth_date)
        session.add(new_user)
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def query_users_db():
    try:
        session = connect_db()
        users = session.query(User).all()
        return users
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def query_user_db(user_id):
    try:
        session = connect_db()
        user = session.query(User).filter_by(id=user_id).first()
        return user
    except Exception as ex:
        print(ex)
    finally:
        disconnect_db(session)

def delete_user_db(user):
    session = connect_db()
    try:
        active_loans = session.query(Loan).filter(
            Loan.user_id == user.id,
            Loan.return_date == None
        ).all()
        
        # here all books are returned by a user before they are deleted
        for loan in active_loans:
            create_return_db(loan.book_id)
        
        session.delete(user)
        session.commit()
    except Exception as ex:
        print(ex)
        session.rollback()
    finally:
        disconnect_db(session)