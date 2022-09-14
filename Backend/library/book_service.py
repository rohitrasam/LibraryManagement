from cmath import exp
from os import stat
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from library.serializers import BookSerializer
from .models import Book

def create_book(request: Request):
    try:
        if Book.objects.filter(**request.data).exists():
            return Response("Book exists in the record", status=status.HTTP_409_CONFLICT)

        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response("Details entered successfully", status=status.HTTP_200_OK)
    except:
        return Response("Failed to enter details", status=status.HTTP_400_BAD_REQUEST)
    
def get_all_books():
    
    books = Book.objects.all()

    if books:
        books_data = BookSerializer(books, many=True)
        return Response(books_data.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_book_info(id: int):
    try:
        book_data = Book.objects.get(id=id)
        if book_data:
            book = BookSerializer(book_data)
            return Response(book.data, status=status.HTTP_200_OK)
    except:
        return Response('Book not found', status=status.HTTP_404_NOT_FOUND)

def update_book_info(request: Request, id: int):

    try:
        book_data = Book.objects.get(id=id)

        updated_book = BookSerializer(instance=book_data, data=request.data)

        if updated_book.is_valid():
            updated_book.save()
            return Response('Book details updated successfully', status=status.HTTP_200_OK)
    except:
        return Response('Failed to update book details', status=status.HTTP_400_BAD_REQUEST)

def remove_book(id: int):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return Response('Deleted book from record', status=status.HTTP_200_OK)
    except:
        return Response('Book does not exist.', status=status.HTTP_404_NOT_FOUND)

    
