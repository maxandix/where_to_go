from django.contrib import admin
from .models import Place, Image

class ImageInline(admin.StackedInline):
    model = Image

class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
