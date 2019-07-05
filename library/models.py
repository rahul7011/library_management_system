from django.db import models

# Create your models here.

class books(models.Model):
    author_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    book_title = models.CharField(max_length=100)
    
class sidebooks(models.Model):
    side_author_name = models.CharField(max_length=100)
    side_img = models.ImageField(upload_to='side')
    side_book_title = models.CharField(max_length=100)
