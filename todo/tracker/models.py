from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=159)
    deadline = models.DateField()
    progress = models.IntegerField(default=0)
