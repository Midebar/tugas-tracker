from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField()
