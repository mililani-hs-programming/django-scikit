from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class file(models.Model):

    upload = models.FileField(upload_to='file')
    filename = models.CharField(max_length=400)

    def __str__(self):
        return self.filename

