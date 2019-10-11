from django import forms
from .models import file

class Files(forms.ModelForm):
    class Meta:
        model = file
        fields = ('upload',)