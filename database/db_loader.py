import pandas as pd
from utils import *

def create_books_df(books):
    df = pd.DataFrame(books)
    df.insert(0, 'id', range(1, len(df) + 1))
    df_books = df[['id', 'title', 'ISBN', 'genre', 'publication_date', 'page_count', 'availability']]
    return df_books

def create_authors_df(books):
    authors_dict = {}
    for book in books:
        authors = book.get('authors', [])
        countries = book.get('author_countries', [])
        for i, author in enumerate(authors):
            country = countries[i] if i < len(countries) else None
            if author not in authors_dict:
                authors_dict[author] = country
    df_authors = pd.DataFrame([
        {'name': author, 'country_of_origin': country} for author, country in authors_dict.items()
    ])
    df_authors.insert(0, 'id', range(1, len(df_authors) + 1))
    return df_authors

def create_book_author_df(books, df_authors):
    author_and_id = df_authors.set_index('name')['id'].to_dict()
    relationship = []
    for idx, book in enumerate(books):
        book_id = idx + 1
        authors = book.get('authors', [])
        for author in authors:
            author_id = author_and_id.get(author)
            if author_id is not None:
                relationship.append({'book_id': book_id, 'author_id': author_id})
    df_book_author = pd.DataFrame(relationship)
    return df_book_author

def create_sql_db(df_books, df_authors, df_book_author, engine):
    df_authors.to_sql('author', engine, if_exists='append', index=False)
    df_books.to_sql('book', engine, if_exists='append', index=False)
    df_book_author.to_sql('book_author', engine, if_exists='append', index=False)