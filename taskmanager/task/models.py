from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    topic = models.CharField(max_length=50)
    description = models.TextField()
    date_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "task"
    def __str__(self):
        return self.topic
