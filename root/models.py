from django.db import models


# Create your models here.
class Root(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
