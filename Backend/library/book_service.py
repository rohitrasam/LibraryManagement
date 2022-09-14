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
    
def get_all_books(request: Request):
    
    print(request.data)
    books = Book.objects.all()

    if books:
        books_data = BookSerializer(books, many=True)
        return Response(books_data.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

def update_book(request: Request):
    