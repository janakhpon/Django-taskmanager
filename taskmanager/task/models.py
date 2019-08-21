from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Task(models.Model):
    topic = models.CharField(max_length=50)
    description = models.TextField()
    date_at = models.DateTimeField(timezone.now() + timezone.timedelta(hours=-24, seconds=-1))
    class Meta:
        db_table = "task"
    def __str__(self):
        return self.topic
