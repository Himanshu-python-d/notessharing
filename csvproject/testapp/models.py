from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact1(models.Model):
    name=models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
