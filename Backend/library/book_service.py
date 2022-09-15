from cmath import exp
from os import stat
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from library.serializers import BookSerializer
from .models import Book

def create_book(request: Request):
    """
    Function to add a book to the db.

    Parameters:
        request (Request): HTTP request that is sent from the frontend

    Returns:
        Response: Success response if the book is added successfully else an error 
                  message with the respective status code.
    """

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
    """
    Function to get all the books from the db.

    Parameters:
        request (Request): HTTP request that is sent from the frontend

    Returns:
        Response: List of books else an error is returned.
    """
    
    books = Book.objects.all()

    if books:
        books_data = BookSerializer(books, many=True)
        return Response(books_data.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_book_info(id: int):
    """
    Function to get the details of a book.

    Parameters:
        id (int): The `id` of the particular book whose details are to be sent.

    Returns:
        Response: HTTP response with details of a book is it is present, else an error message is returned.
    """

    try:
        book_data = Book.objects.get(id=id)
        if book_data:
            book = BookSerializer(book_data)
            return Response(book.data, status=status.HTTP_200_OK)
    except:
        return Response('Book not found', status=status.HTTP_404_NOT_FOUND)

def update_book_info(request: Request, id: int):
    """
    Function to update the book details.

    Parameters:
        request (Request): HTTP request that is sent from the frontend.
        id (int): The `id` of the particular book whose details are to be updated.

    Returns:
        Response: HTTP response with the appropriate messasge and status code.
    """

    try:
        book_data = Book.objects.get(id=id)

        updated_book = BookSerializer(instance=book_data, data=request.data)

        if updated_book.is_valid():
            updated_book.save()
            return Response('Book details updated successfully', status=status.HTTP_200_OK)
    except:
        return Response('Failed to update book details', status=status.HTTP_400_BAD_REQUEST)

def remove_book(id: int):
    """
    Function to delete a book frpm the db.

    Parameters:
        id (int): The `id` of that particular book that is to be deleted from the db.

    Returns:
        Response: HTTP response with the appropriate messasge and status code.
    """
    
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return Response('Deleted book from record', status=status.HTTP_200_OK)
    except:
        return Response('Book does not exist.', status=status.HTTP_404_NOT_FOUND)

    
