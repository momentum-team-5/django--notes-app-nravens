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

# Add the ability to search notes and get back a list of notes that match your search text (case-insensitive).
class SearchForm(forms.Form):
    
    # This tuple provides selections for ordering the results
    ORDER_CHOICES = (
        ("title", "title"),
        ("updated_at", "updated at"),
    )

    # Form fields
    # * Add the ability to sort your notes by title or by updated at (descending or ascending).

    title = forms.CharField(max_length=255, required=True)
    #title_search_type = "starts with"
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)
    
    
    # def clean(self):
    #     """
    #     Require at least one of title and body to be non-blank.
    #     """

    #     cleaned_data = super().clean()
    #     cleaned_title = cleaned_data['title']
    #     #cleaned_body = cleaned_data['body']

    #     #if cleaned_title or cleaned_body:
    #     return cleaned_t

        #raise ValidationError('At least one search field must be specified', code='invalid')
