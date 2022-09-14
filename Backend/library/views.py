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
    res = get_all_books(request)
    return Response(res.data, status=res.status_code)