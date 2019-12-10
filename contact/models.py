from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
