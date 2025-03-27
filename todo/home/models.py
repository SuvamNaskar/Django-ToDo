from django.db import models

class Tasks(models.Model):
    task = models.CharField(max_length=255)
    status = models.IntegerField(default=0)