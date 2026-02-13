from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    isPublish = models.BooleanField(default=True)

    def __str__(self):
        return self.name
