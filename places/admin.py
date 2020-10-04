from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview"]

    @staticmethod
    def image_preview(obj):
        preview_height = 200
        return format_html('<img src="{url}" width="{width}px" height={height}px />',
                           url=obj.img.url,
                           width=obj.img.width / obj.img.height * preview_height,
                           height=preview_height,
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview"]

    @staticmethod
    def image_preview(obj):
        preview_height = 200
        return format_html('<img src="{url}" width="{width}" height={height} />',
                           url=obj.img.url,
                           width=obj.img.width / obj.img.height * preview_height,
                           height=preview_height,
                           )
