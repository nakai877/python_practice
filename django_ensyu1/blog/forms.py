from django import forms
from .models import Tag, Article

class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('name',)

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','text', 'category', 'tags')

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','text', 'category', 'tags')
