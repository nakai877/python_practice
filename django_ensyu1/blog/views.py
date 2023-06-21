from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.shortcuts import redirect

from .forms import TagCreateForm, ArticleCreateForm, ArticleUpdateForm, SearchForm,CommentCreateForm
from .models import Article, Tag, Comment

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'blog/home.html'

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')
        if keyword:
            #完全一致=>title, 部分一致=>title__icontains
            queryset = queryset.filter(
                #from django.db.models import Q で下記のようにor検索できる
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class TagListView(generic.ListView):
    model = Tag
    template_name = 'blog/tag_list.html'

class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:home')  # テンプレートで使った、urlタグみたいなもの
    form_class = TagCreateForm

class ArticleCreateView(generic.CreateView):
    model = Tag
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = ArticleCreateForm

class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:article_list')
    form_class = CommentCreateForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.target = Article.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('blog:article_list')

class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class =  ArticleUpdateForm
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')


class ArticleDeleteView(generic.DeleteView):
    # フォームは必要なし
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article_list')


