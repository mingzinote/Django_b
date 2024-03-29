from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    
class Habit(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField(default=timezon.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# Create your models here.
