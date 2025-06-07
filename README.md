# 📚 Library Management System

A command-line interface application for managing a small library. It allows for user and book management, as well as handling loans and returns. The initial book data is scraped from a public website and stored in a SQLite database.

---

## Features

- **Database Population**: Automatically scrapes book data from a website to populate the database.
- **Book Management**: Lists all available books.
- **User Management**: Register new users and delete existing ones.
- **Loan System**: Create and track book loans and returns.
- **View History**: List all active and closed (returned) loans.
- **Relational Database**: Uses a relational model with Books, Authors, Users, and Loans.

---

### Core Libraries:

- `SQLAlchemy`: For Object-Relational Mapping (ORM) and database interaction.  
- `pandas`: For structuring scraped data before database insertion.  
- `BeautifulSoup`: For web scraping book information.

---

## Project Structure

The project is organized into a main application module and a database package that handles data persistence and modeling.

```
/
├── database/
│ ├── books_scraper.py # Script to scrape data and create the DB
│ ├── db_loader.py # Helper to process data with Pandas
│ ├── models.py # SQLAlchemy ORM models
│ └── example_queries.py # Standalone SQL query examples
│
├── crud_books.py # Functions for book-related views
├── crud_books_db.py
├── crud_loans.py # Functions for loan-related views
├── crud_loans_db.py
├── crud_users.py # Functions for user-related views
├── crud_users_db.py
├── db_connector.py # Handles DB session connection
├── main.py # Main entry point for the application
├── menu.py # Displays the main menu
└── utils.py # Utility functions (date parsing, etc.)
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

```

### 2. Install the required packages
```bash
pip install sqlalchemy beautifulsoup4 pandas
```

### 3. Create and Populate the Database
Run the web scraper script from the project's root directory. This will create a library.db file inside the database/ folder and populate it with book data.

```bash
python -m database.books_scraper
```
You should see a confirmation message:
> Data inserted into the "library.db" database.

### Interact with the menu:
The application will present you with a menu of options. Enter the number corresponding to the action you wish to perform.

```mathematica
+==================================+
|            Welcome!              |
+==================================+

1 - List books
2 - List users
3 - List active loans
4 - List closed loans
5 - Register user
6 - Delete user
7 - Create loan
8 - Create return
0 - Exit

Enter the desired option:
````

### Database Schema
The application uses five main tables to manage the library's data:

**book:** Stores information about each book (title, ISBN, availability, etc.).

**author:** Stores author details (name, country of origin).

**user:** Stores library user information.

**loan:** Tracks which user has borrowed which book, including loan and return dates.

**book_author:** A many-to-many relationship table linking books to their authors.

