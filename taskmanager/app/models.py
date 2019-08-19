from django.db import models
from django.utils import timezone

class Task(models.Model):
    topic = models.CharField(max_length=50)
    description = models.TextField()
    date_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'TOPIC : {}'.format(self.topic)
