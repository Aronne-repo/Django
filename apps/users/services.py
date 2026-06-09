from .models import Author, Book
from rest_framework.exceptions import NotFound

def get_all_authors():
    return Author.objects.all()

def get_author_by_id(author_id):
    try:
        return Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise NotFound("Autore non trovato")

def create_author(validated_data):
    return Author.objects.create(**validated_data)

def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise NotFound("Libro non trovato")