from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    # assuming you're using some form of image handling
    image = models.ImageField(upload_to='artists/')

    def __str__(self):
        return self.name
