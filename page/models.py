from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    pass


class Reservation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="owner")
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    no_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


    def _str_(self):
        return self.owner.username

class category(models.Model):
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.item



class Menu(models.Model):
    item_name = models.CharField(max_length=30)
    itme_description = models.TextField()
    item_price = models.FloatField()
    item_img = models.TextField()
    item_category = models.ForeignKey(category,on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return self.item_name