from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    # all_tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Note
        fields = ['title', 'text', 'tags']