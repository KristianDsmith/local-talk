from django.contrib import admin
from .models import Record, Artist, BlogPost


class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date',
                    'get_categories_display', 'download_link', 'vinyl_link')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['category'].widget.attrs['class'] = 'checkbox-inline'
        return form

    def download_link(self, obj):
        if 'LATEST' in obj.category or 'SINGLE' in obj.category:
            if obj.download_link:
                return format_html('<a href="{}">Download</a> - £{:.2f}', obj.download_link, obj.download_price)
        return ''

    download_link.short_description = 'Download Link'

    def vinyl_link(self, obj):
        if 'LATEST' in obj.category or 'SINGLE' in obj.category:
            if obj.vinyl_link:
                return format_html('<a href="{}">Vinyl</a> - £{:.2f}', obj.vinyl_link, obj.vinyl_price)
        return ''

    vinyl_link.short_description = 'Vinyl Link'

    def get_categories_display(self, obj):
        return ', '.join(obj.category)

    get_categories_display.short_description = 'Categories'


admin.site.register(Artist)
admin.site.register(Record, RecordAdmin)
admin.site.register(BlogPost)
