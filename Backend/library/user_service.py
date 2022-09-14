from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from library.serializers import UserModelSerializer, UserSerializer
from .models import User


def add_user(request: Request):
    try:
        if User.objects.filter(**request.data).exists():
            return Response("User already exists", status=status.HTTP_409_CONFLICT)

        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response("Account created", status=status.HTTP_200_OK)
    except:
        return Response('Failed to create account', status=status.HTTP_400_BAD_REQUEST)


def get_user(request: Request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email)
        if user.password != password:
            return Response("Wrong password", status=status.HTTP_404_NOT_FOUND)
            
        user = UserModelSerializer(user)
        return Response(user.data, status=status.HTTP_200_OK)
    except:
        return Response('User not found', status=status.HTTP_404_NOT_FOUND)