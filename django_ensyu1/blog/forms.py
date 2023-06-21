from django import forms
from .models import Tag, Article,Comment

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

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text')