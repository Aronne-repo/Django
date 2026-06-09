from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import (
    get_all_authors,
    get_author_by_id,
    create_author,
    get_all_books,
    get_book_by_id)
from .serializers import AuthorSerializer, BookSerializer

@api_view(['GET'])
def get_authors(request):
    authors = get_all_authors()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_author(request, author_id):
    author = get_author_by_id(author_id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['POST'])
def create_author_view(request):
    serializer = AuthorSerializer(data=request.data)

    if serializer.is_valid():
        author = create_author(serializer.validated_data)
        return Response(AuthorSerializer(author).data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_books(request):
    books = get_all_books()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, book_id):
    book = get_book_by_id(book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)