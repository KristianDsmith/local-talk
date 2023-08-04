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