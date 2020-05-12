from django.db import models


class Rule(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.CharField(max_length=150, null=True)
    callNo = models.CharField(max_length=20, null=True)
    desc = models.CharField(max_length=250, null=True)
    disabled = models.BooleanField(null=True)
    href = models.CharField(max_length=150, null=True)
    key = models.IntegerField(null=True)
    name = models.CharField(max_length=150, null=True)
    owner = models.CharField(max_length=150, null=True)
    progress = models.SmallIntegerField()
    status = models.SmallIntegerField()
    title = models.CharField(max_length=150, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

