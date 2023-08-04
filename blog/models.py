from django.urls import reverse
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    # assuming you're using some form of image handling
    image = models.ImageField(upload_to='artists/')

    def __str__(self):
        return self.name

class Record(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='record_covers/', blank=True, null=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LatestRelease(models.Model):
    image = models.ImageField(
        upload_to='images/releases/', blank=True, null=True)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, default=None, null=True)
    download_link = models.URLField(
        default='https://example.com/default-download-link')
    download_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    vinyl_link = models.URLField(
        default='https://example.com/default-vinyl-link')
    vinyl_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    release_date = models.DateField()

    def __str__(self):
        return self.title
