from django.db import models

# Create your models here.
# This is the model for the notes
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# This is the string representation of the object
    def __str__(self):
        return self.body[0:20]
    