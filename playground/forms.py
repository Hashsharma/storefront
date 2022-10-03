
from django import forms
from . import models
 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = models
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]