from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField()
    def __str__(self):
        return self.name