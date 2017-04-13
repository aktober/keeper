from rest_framework import serializers

from notes.models import Tag, Note


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']

    def validate_tag(self, value):
        tag = value
        qs = Tag.objects.filter(tag__exact=tag)
        if qs.exists():
            raise serializers.ValidationError('This tag already exists')
        return tag


class NoteSerializer(serializers.ModelSerializer):
    all_tags = serializers.StringRelatedField(many=True)
    # all_tags = TagSerializer(many=True)

    class Meta:
        model = Note
        fields = ['title', 'text', 'all_tags']