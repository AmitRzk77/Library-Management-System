# Library-Management-System# Library Management System

A Library Management System built using Django and Django REST Framework (DRF). This system provides APIs to manage various aspects of a library, including authors, books, genres, transactions, reviews, stock, volume, and publications.

## Features

- **Authors**: Manage authors and their details.
- **Books**: Manage books, including their titles, authors, genres, and more.
- **Genres**: Define genres for categorizing books.
- **Transactions**: Handle borrowing and returning of books.
- **Reviews**: Allow users to leave reviews for books.
- **Stock**: Track the number of books available in the library.
- **Volume**: Manage volumes of books (e.g., multiple editions).
- **Publications**: Manage book publishers and publications.

## API Endpoints

The system exposes the following API endpoints:

- **Authors**:  
  `GET /api/authors/` - List all authors  
  `POST /api/authors/` - Create a new author  
  `GET /api/authors/{id}/` - Retrieve a specific author  
  `PUT /api/authors/{id}/` - Update a specific author  
  `DELETE /api/authors/{id}/` - Delete a specific author

- **Books**:  
  `GET /api/books/` - List all books  
  `POST /api/books/` - Create a new book  
  `GET /api/books/{id}/` - Retrieve a specific book  
  `PUT /api/books/{id}/` - Update a specific book  
  `DELETE /api/books/{id}/` - Delete a specific book

- **Genres**:  
  `GET /api/genres/` - List all genres  
  `POST /api/genres/` - Create a new genre  
  `GET /api/genres/{id}/` - Retrieve a specific genre  
  `PUT /api/genres/{id}/` - Update a specific genre  
  `DELETE /api/genres/{id}/` - Delete a specific genre

- **Transactions**:  
  `GET /api/transactions/` - List all transactions  
  `POST /api/transactions/` - Create a new transaction  
  `GET /api/transactions/{id}/` - Retrieve a specific transaction  
  `PUT /api/transactions/{id}/` - Update a specific transaction  
  `DELETE /api/transactions/{id}/` - Delete a specific transaction

- **Reviews**:  
  `GET /api/reviews/` - List all reviews  
  `POST /api/reviews/` - Create a new review  
  `GET /api/reviews/{id}/` - Retrieve a specific review  
  `PUT /api/reviews/{id}/` - Update a specific review  
  `DELETE /api/reviews/{id}/` - Delete a specific review

- **Stock**:  
  `GET /api/stock/` - List all stock items  
  `POST /api/stock/` - Create a new stock item  
  `GET /api/stock/{id}/` - Retrieve a specific stock item  
  `PUT /api/stock/{id}/` - Update a specific stock item  
  `DELETE /api/stock/{id}/` - Delete a specific stock item

- **Volume**:  
  `GET /api/volume/` - List all volumes  
  `POST /api/volume/` - Create a new volume  
  `GET /api/volume/{id}/` - Retrieve a specific volume  
  `PUT /api/volume/{id}/` - Update a specific volume  
  `DELETE /api/volume/{id}/` - Delete a specific volume

- **Publications**:  
  `GET /api/publications/` - List all publications  
  `POST /api/publications/` - Create a new publication  
  `GET /api/publications/{id}/` - Retrieve a specific publication  
  `PUT /api/publications/{id}/` - Update a specific publication  
  `DELETE /api/publications/{id}/` - Delete a specific publication

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

Your API will be available at `http://127.0.0.1:8000/api/`.

## Testing

To run tests, use:
```bash
python manage.py test
