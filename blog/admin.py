from django.contrib import admin
from django.utils.html import format_html
from .models import Artist, Record, BlogPost, LatestRelease


class LatestReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_artist', 'display_image',
                    'download_link', 'vinyl_link')

    def display_artist(self, obj):
        if obj.artist:
            return obj.artist.name
        return None

    display_artist.short_description = 'Artist'

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return None

    display_image.short_description = 'Image'

    def download_link(self, obj):
        if obj.download_link:
            return format_html('<a href="{}">Download</a> - ${}', obj.download_link, obj.download_price)
        return ''

    download_link.short_description = 'Download Link'

    def vinyl_link(self, obj):
        if obj.vinyl_link:
            return format_html('<a href="{}">Vinyl</a> - ${}', obj.vinyl_link, obj.vinyl_price)
        return ''

    vinyl_link.short_description = 'Vinyl Link'


admin.site.register(Artist)
admin.site.register(Record)
admin.site.register(BlogPost)
admin.site.register(LatestRelease, LatestReleaseAdmin)
