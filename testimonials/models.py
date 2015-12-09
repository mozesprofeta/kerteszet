from django.db import models

# Create your models here.


class Opinion(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
