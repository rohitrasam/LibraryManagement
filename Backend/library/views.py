from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .user_service import *
from .book_service import *

# Create your views here.

@api_view(['POST'])
def create_user(request: Request):
    res = add_user(request)

    return Response(res.data, status=res.status_code)

@api_view(['POST'])
def login(request: Request):
    res = get_user(request)

    return Response(res.data, status=res.status_code)


@api_view(['POST'])
def add_book(request: Request):

    res = create_book(request)
    return Response(res.data, status=res.status_code)

@api_view(['GET'])
def get_books(request: Request):

    res = get_all_books()
    return Response(res.data, status=res.status_code)

@api_view(['GET'])
def get_book(request: Request, id: int):
    res = get_book_info(id)

    return Response(res.data, status=res.status_code)

@api_view(['PATCH'])
def update_book(request: Request, id: int):

    res = update_book_info(request, id)
    return Response(res.data, status=res.status_code)

@api_view(['DELETE'])
def delete_book(request: Request, id: int):

    res = remove_book(id)
    return Response(res.data, status=res.status_code)