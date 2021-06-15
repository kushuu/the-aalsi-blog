from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
import django

from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length = 13)
    message = models.CharField(max_length=250)
    date = models.DateTimeField()

    def __str__(self):
        return self.email

class Articles(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(null = True, blank = True, upload_to = 'static/images/')
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=500, default="")
    article_body = RichTextField(blank = True, null = True)
    likes = models.IntegerField(default=0, blank=True)
    date_added = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title
