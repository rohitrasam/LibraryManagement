from django.db import models

# Create your models here.
class User(models.Model):
    """
    A class to create `User` table in the DB.

    Attributes:
        id (int): An auto generated, unique field which is the primary key for the User table
        name (str): Column with the names of the user.
        email (str): Column with the email id of the user.
        ph_no (str): It contains the phone number of the user.
        password (str): Stores the password of the user.
        isAdmin (bool): Whether the user is admin or not
    """

    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    ph_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    isAdmin = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}, {self.name}"

class Book(models.Model):
    """
    A class to create a `Book` table in the DB.

    Attributes:
        id (int): An auto generated, unique field which is the primary key for the Book table
        name (str): Column with the names of the book.
        author (str): Column with the author name of the book.
        price (float): Stores the price of the book.
        description (str): It contains a short description about the book.
        image (str): Stores image link of the book cover.
        quantity (int): Contains the number of books present in the Library.
    """
    
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=200, default="")
    image = models.TextField(default="")
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.id}, {self.name}"

