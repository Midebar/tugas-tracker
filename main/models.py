from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=150)
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField()
