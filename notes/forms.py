from django import forms
from notes.models import Note, Tag


class NewNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Text'}


class NewTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
