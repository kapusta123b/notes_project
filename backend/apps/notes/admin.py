from django.contrib import admin

from apps.notes.models.note import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Information', {
            'fields': ('title', 'content')
        }),
        ('Date', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse'),
        }),
    )