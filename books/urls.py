from django.urls import path
from .views import book_list, edit_book

urlpatterns = [
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('', book_list, name='book_list'),
]

