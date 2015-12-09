from django.db import models

# Create your models here.


class Customer (models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
