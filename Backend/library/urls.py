from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.create_user, name='create-user'),
    path('login/', views.login, name='user-login'),
    path('add_book/', views.add_book, name='add-book'),
    path('get_books/', views.get_books, name='get-all-books')
]
