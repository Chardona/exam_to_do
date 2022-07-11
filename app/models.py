from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag)

    class Meta:
        ordering = ['done', '-datetime']
