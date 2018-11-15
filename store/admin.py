from django.contrib import admin

from .models import File


class FileAdmin(admin.ModelAdmin):
    fields = ["name", "path"]
    list_display = ('name', 'date', 'path')

admin.site.register(File, FileAdmin)
