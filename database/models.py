from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    ISBN = Column(String(20), nullable=False)
    genre = Column(String(50))
    publication_date = Column(Date)
    page_count = Column(Integer)
    availability = Column(Integer, nullable=False)
    
    loans = relationship("Loan", back_populates="book")
    book_authors = relationship("Book_Author", back_populates="book")

class Author(Base):
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    country_of_origin = Column(String(20))
    
    book_authors = relationship("Book_Author", back_populates="author")

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    
    loans = relationship("Loan", back_populates="user", cascade="all, delete-orphan")

class Loan(Base):
    __tablename__ = 'loan'
    
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    loan_date = Column(DateTime, primary_key=True)
    return_date = Column(DateTime)
    
    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")

class Book_Author(Base):
    __tablename__ = 'book_author'
    
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    
    book = relationship("Book", back_populates="book_authors")
    author = relationship("Author", back_populates="book_authors")