from rest_framework import serializers
from .models import Book, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'nationality']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'isbn',
            'publication_year',
            'pages',
            'language',
            'category',
            'authors'
        ]

class BookWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category')

    author_ids = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        many=True,
        source='authors')

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'isbn',
            'publication_year',
            'pages',
            'language',
            'category_id',
            'author_ids'
        ]