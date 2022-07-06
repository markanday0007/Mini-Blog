from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc =models.TextField()
    created = models.DateTimeField(auto_now_add=True)