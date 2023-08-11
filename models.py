from django.db import models

class TextInput(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
