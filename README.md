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

