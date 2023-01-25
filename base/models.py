from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Status(models.Model):
    status=models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    description=RichTextField(max_length=200, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    status=models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)

    def display_status(self):
        if self.status.status == 'Available':
            return 'green'
        else:
            return 'red'
    
    def __str__(self):
        return self.name

class Namaz(models.Model):
    name=models.CharField(max_length=15)
    time=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Notification(models.Model):
    subject=models.CharField(max_length=100)
    body=RichTextField(max_length=300)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject

class Mosque(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    adress=RichTextField(max_length=50)
    phone=models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name



