from django.core.validators import FileExtensionValidator
from django.db import models
import os

# Create your models here.

class Video(models.Model):
    file = models.FileField(null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.file.name
