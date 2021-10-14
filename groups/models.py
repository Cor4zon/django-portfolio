from django.db import models

# Create your models here.
class AlbumCard(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=50)
    year = models.DateField()
    cover = models.FilePathField(path="")
