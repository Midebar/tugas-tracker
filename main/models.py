from django.db import models

class Item(models.Model):
    name = models.CharField()
    amount = models.IntegerField
    description = models.TextField
