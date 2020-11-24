from django.db import models

# Create your models here.

class todo(models.Model):

    Date_id=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
