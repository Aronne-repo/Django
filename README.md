# Django Library API 

REST API built with Django and Django REST Framework.
The project manages a simple library system with books, authors and categories.
It follows a layered architecture, with clear separation between views, services, models and serializers.

---

## Technical Stack

Python 3.13  
Django 6  
Django REST Framework  
SQLite (default Django DB)  
python-dotenv (environment config)  
Layered architecture (Model → Service → View → Serializer)

---

## Project Structure
```
DJANGO/
│
├── apps/
│   └── users/
│       ├── models.py        # Database models (entities)
│       ├── serializers.py   # DTO + mapping
│       ├── services.py      # Business logic
│       ├── views.py         # API endpoints
│       ├── urls.py          # App routing
│       └── migrations/
│
├── config/
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Root routing
│
├── manage.py
├── requirements.txt
├── .env
└── db.sqlite3
```

---

## Architecture Overview

The project uses a layered approach:
```
View (Controller) → Service → Model
↓
Serializer
```

- Models → Database entities
- Serializers → DTO + mapping
- Services → Business logic
- Views → REST endpoints

---

## Database

The project uses SQLite for development.
Database file:
```
db.sqlite3
```

## Installation

Clone the repository:
```
git clone 
cd DJANGO
```
---

## Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```
---

## Install dependencies
```
pip install -r requirements.txt
```
---

## Configure environment

Create a `.env` file containing:
```
DEBUG=True
SECRET_KEY=your-secret-key
```
---

## Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```
---

## Run the application
```
python manage.py runserver
```

Server will start at:
```
http://127.0.0.1:8000/
```

---

## API Endpoints

**Authors**
GET /api/authors/           → Get all authors
GET /api/authors/{id}/      → Get author by ID
POST /api/authors/create/   → Create new author

---

**Books**
GET /api/books/             → Get all books
GET /api/books/{id}/        → Get book by ID

---

## Example Requests

**Create Author**
POST `/api/authors/create/`

```json
{
  "first_name": "George",
  "last_name": "Orwell",
  "birth_date": "1903-06-25",
  "nationality": "British"
}
```

**Get Books**
GET `/api/books/`

Response:
```json
[
  {
    "id": 1,
    "title": "1984",
    "isbn": "1234567890123",
    "publication_year": 1949,
    "pages": 300,
    "language": "EN",
    "category": {
      "id": 1,
      "name": "Dystopian"
    },
    "authors": [
      {
        "id": 1,
        "first_name": "George",
        "last_name": "Orwell"
      }
    ]
  }
]
```

## Notes

- Nested serializers are used for read operations
- Separate write serializer is used for Book creation (ID-based relationships)
- ManyToMany relationships are handled using primary key references
- SQLite is used for development only
- .env file is required for configuration
