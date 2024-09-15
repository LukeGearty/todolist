from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name