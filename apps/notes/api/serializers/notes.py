from rest_framework import serializers
from django.utils.html import escape
from apps.notes.models.note import Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


    def validate_title(self, value):
        if not value.strip():
            return serializers.ValidationError('The title must not be empty')
        return escape(value.strip())
    
    def validate_content(self, value):
        if not value.strip():
            return serializers.ValidationError('The content must not be empty')
        return escape(value.strip())
        


class NoteCreateSerializer(NoteSerializer):
    pass


class NoteUpdateSerializer(NoteSerializer):
    title = serializers.CharField(required=False)
    context = serializers.CharField(required=False)
    