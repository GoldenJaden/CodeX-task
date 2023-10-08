from django.forms import ModelForm
from django import forms
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
