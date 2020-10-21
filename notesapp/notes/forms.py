from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Model form for the Poem class used for create and update operations.
    """
    class Meta:
        model = Note
        fields = [
            'title',
            'body'
        ]