from django import forms
from django.urls import reverse
from django.contrib import admin
from django.db import models
from django.utils.html import format_html


class Artist(models.Model):
    name = models.CharField(max_length=200)
    # assuming you're using some form of image handling
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    CATEGORY_CHOICES = (
        ('ALBUM', 'Album'),
        ('LATEST', 'Latest Release'),
        ('SINGLE', 'Single'),
    )

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(
        upload_to='record_covers/', blank=True, null=True)
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default='LATEST', blank=True)
    download_link = models.URLField(blank=True, null=True)
    download_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    vinyl_link = models.URLField(blank=True, null=True)
    vinyl_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title


class RecordAdminForm(forms.ModelForm):
    CATEGORY_CHOICES = (
        ('ALBUM', 'Album'),
        ('LATEST', 'Latest Release'),
        ('SINGLE', 'Single'),
    )

    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Record
        fields = '__all__'

class RecordAdmin(admin.ModelAdmin):
    form = RecordAdminForm
    list_display = ('title', 'artist', 'release_date',
                    'category', 'download_link', 'vinyl_link')

    def download_link(self, obj):
        if 'LATEST' in obj.category or 'SINGLE' in obj.category:
            # Handle the download link logic here
            return format_html('<a href="{}">Download</a>', 'your_download_link')
        return ''

    download_link.short_description = 'Download Link'

    def vinyl_link(self, obj):
        if 'LATEST' in obj.category or 'SINGLE' in obj.category:
            # Handle the vinyl link logic here
            return format_html('<a href="{}">Vinyl</a>', 'your_vinyl_link')
        return ''

    vinyl_link.short_description = 'Vinyl Link'


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
