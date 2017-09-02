from django import forms
from .models import problemPost

class PostForm(forms.ModelForm):
    
    class Meta:
        model = problemPost
        fields = ('rollNumber', 'problemType','detail')
