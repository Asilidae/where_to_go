from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('image', 'get_preview', 'number',)
    admin.TabularInline.extra = 0

    def get_preview(self, obj):
        return mark_safe(
            '<img src="{url}" height={height} />'.format(
                url=obj.image.url,
                height='200px'
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [ImageInline]
