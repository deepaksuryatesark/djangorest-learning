from django.db import models

class Blog(models.Model):
    title =  models.CharField(max_length=200)
    desc =  models.CharField(max_length=1000)
    author =  models.CharField(max_length=50)