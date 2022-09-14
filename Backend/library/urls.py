from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.create_user, name='create-user'),
    path('login/', views.login, name='user-login'),
    path('add_book/', views.add_book, name='add-book'),
    path('get_books/', views.get_books, name='get-all-books'),
    path('get_book/<int:id>', views.get_book, name='get-book'),
    path('update_book/<int:id>', views.update_book, name='update-book'),
    path('delete_book/<int:id>', views.delete_book, name='delete-book')
]
