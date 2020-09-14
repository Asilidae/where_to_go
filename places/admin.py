from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('image', 'get_preview', 'number',)
    admin.TabularInline.extra = 1

    def get_preview(self, obj):
        return mark_safe(obj.get_image())


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [ImageInline]
