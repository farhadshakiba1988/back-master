from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    signature = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    notifyCount = models.IntegerField()
    unreadCount = models.IntegerField()
    tags = ArrayField(JSONField(), null=True)
