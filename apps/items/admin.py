from django.contrib import admin
from .models import Item, Photo,Tag

class PhotoInline(admin.TabularInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)    
admin.site.register(Photo)
admin.site.register(Tag)
