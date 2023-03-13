from django.db import models


class Todo(models.Model):
    """A model represent the todo object contains title and body"""

    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"
