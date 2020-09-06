from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image
# Register your models here.


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('image', 'get_preview', 'number',)

    def get_preview(self, obj):
        return mark_safe(
            '<img src="{url}" height={height} />'.format(
                url=obj.image.url,
                height='200px',
            )
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

