from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    parent = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {'Completed' if self.status else 'Pending'}"
