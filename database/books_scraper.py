from sqlalchemy import create_engine
from bs4 import BeautifulSoup

from database.db_loader import *
from database.models import Base


URL = 'https://pedrovncs.github.io/livrariapython/livros.html'

engine = create_engine('sqlite:///database/my_library.db', echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

html = access_url(URL)
soup = BeautifulSoup(html, "html.parser")

books = []
li_list = soup.find("ul", id="livros-lista").find_all("li")
for li in li_list:
    div = li.find('div')
    title = div.find('h5').get_text(strip=True)
    book = {'title': title}
    ps = div.find_all('p')
    for p in ps:
        strong = p.find('strong')
        if not strong:
            continue
        field = strong.get_text(strip=True).replace(":", "")
        value = p.get_text(strip=True).replace(strong.get_text(strip=True), "").strip()
        if field == "ISBN":
            book['ISBN'] = value
        elif field == "Gênero":
            book['genre'] = value
        elif field == "Autor(es)":
            book['authors'] = [a.strip() for a in value.split(',')]
        elif field == "País de Nascimento":
            book['author_countries'] = [p.strip() for p in value.split(',')]
        elif field == "Data de publicação":
            book['publication_date'] = process_scraped_date(value)
        elif field == "Páginas":
            book['page_count'] = int(value)
        elif field == "Quantidade Disponível":
            book['availability'] = int(value)
    books.append(book)

df_books = create_books_df(books)
df_authors = create_authors_df(books)
df_book_author = create_book_author_df(books, df_authors)

create_sql_db(df_books, df_authors, df_book_author, engine)

print("\nData inserted into the \"library.db\" database.")