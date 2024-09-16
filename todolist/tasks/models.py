from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def mark_completed(self):
        self.completed = True
        self.date_completed = timezone.now()
        self.save()