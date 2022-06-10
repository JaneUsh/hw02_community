from django import forms
from .models import Group


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False, empty_label='')
