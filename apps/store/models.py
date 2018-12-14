from django.db import models

from django.conf import settings


class File(models.Model):
    name = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    path = models.FileField(upload_to="store")

    def __str__(self):
        return self.name
