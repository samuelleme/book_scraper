from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_db():
    engine = create_engine('sqlite:///database/my_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def disconnect_db(session):
    if session:
        session.close()