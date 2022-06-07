from django import forms
from .models import Post, Group


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].required = False
        self.fields['group'] = forms.ModelChoiceField(
            queryset=Group.objects.all()
        )
        self.fields['group'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ['group', 'text']
