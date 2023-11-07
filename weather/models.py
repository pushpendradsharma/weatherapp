from django.db import models
from django.contrib.auth.models import User

class SearchData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
