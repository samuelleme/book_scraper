import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def query_books_and_authors(engine):
    # books with their authors
    query1 = """
    SELECT b.title, a.name AS author, b.availability
    FROM book b
    JOIN book_author ba ON b.id = ba.book_id
    JOIN author a ON ba.author_id = a.id;
    """
    df_books_authors = pd.read_sql_query(query1, engine)
    print("\nBooks with their authors:")
    print(df_books_authors)
    
def query_books_by_genre(engine):
    # count of books by genre
    query2 = """
    SELECT genre, COUNT(*) AS total_books
    FROM book
    GROUP BY genre;
    """
    df_books_genre = pd.read_sql_query(query2, engine)
    print("\nCount of books by genre:")
    print(df_books_genre)
    
def query_author_book_count(engine):
    # authors and number of books written
    query3 = """
    SELECT a.name, COUNT(ba.book_id) AS total_books
    FROM author a
    LEFT JOIN book_author ba ON a.id = ba.author_id
    GROUP BY a.name;
    """
    df_authors_count = pd.read_sql_query(query3, engine)
    print("\nAuthors and number of books written:")
    print(df_authors_count)
    
def query_top5_available_books(engine):
    # top 5 books with the highest availability
    query4 = """
    SELECT title, availability
    FROM book
    ORDER BY availability DESC
    LIMIT 5;
    """
    df_top_availability = pd.read_sql_query(query4, engine)
    print("\nTop 5 books with highest availability:")
    print(df_top_availability)

# Tests
engine = create_engine('sqlite:///database/my_library.db')
Session = sessionmaker(bind=engine)
session = Session()

query_books_and_authors(engine)
query_books_by_genre(engine)
query_author_book_count(engine)
query_top5_available_books(engine)