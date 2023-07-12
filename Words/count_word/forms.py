from django import forms

from .models import FileRequest


class FileRequestForm(forms.ModelForm):
    class Meta:
        model = FileRequest
        fields = ('file', 'word_to_find')
