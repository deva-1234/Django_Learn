from django.db import models

# Create your models here.

class blog1(models.Model):

    Title=models.CharField(max_length=200)
    Name=models.CharField(max_length=200)
    Age=models.CharField(max_length=200)

    def __str__(self):
        return self.Title
