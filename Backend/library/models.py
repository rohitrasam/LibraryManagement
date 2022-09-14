from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    ph_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    isAdmin = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}, {self.name}"

class Book(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=200, default="")
    image = models.TextField(default="")
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.id}, {self.name}"

