from django.contrib import admin

from webapp.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'status', 'created_at']
    list_filter = ['created_at', 'status']
    search_fields = ['text', 'name']
    fields = ['name', 'email', 'text', 'status']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Note, NoteAdmin)

# Register your models here.
