from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_authors),
    path('authors/<int:author_id>/', views.get_author),
    path('authors/create/', views.create_author_view),
    path('books/', views.get_books),
    path('books/<int:book_id>/', views.get_book)
]