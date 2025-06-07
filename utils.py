from urllib.request import urlopen, Request
from datetime import datetime

def process_scraped_date(date_str):
    try:
        dt = datetime.strptime(date_str.strip(), '%d-%m-%Y')
    except ValueError:
        try:
            dt = datetime.strptime(date_str.strip(), '%Y')
        except ValueError:
            return None
    return dt.date()

def access_url(URL):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(URL, headers=headers)
        html = urlopen(req)
    except Exception as ex:
        print(f"! Error: URL access ! - {ex}")
        exit()
    return html

def insert_user_id(message):
    try:
        user_id = int(input(message))
    except ValueError:
        print("! Invalid ID !")
        return None
    return user_id

def insert_book_id(message):
    try:
        book_id = int(input(message))
    except ValueError:
        print("! Invalid ID !")
        return None
    return book_id

def insert_birth_date(message):
    date_str = input(message).strip()
    try:
        birth_date = datetime.strptime(date_str, "%d-%m-%Y").date()
        return birth_date
    except ValueError:
        print("! Error: invalid date format! Use dd-mm-yyyy.")
        return None