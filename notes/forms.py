from django import forms
from notes.models import Note


class NewNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'tags']
