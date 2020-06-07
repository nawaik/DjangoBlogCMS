from django import forms

from .models import Articles, Comments

class CreateArticleForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ('title', 'text', 'meta_title', 'meta_description')

class CreateCommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('author', 'email', 'comment')
        labels = {'author': 'Naam', 'email': 'E-mailadres', 'Comment': 'Reactie'}