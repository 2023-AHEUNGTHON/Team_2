from django.shortcuts import render, redirect
from articles.models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    commnets = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : commnets,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = {'form' : form}
    return render(request, 'articles/create.html', context)

def update(request, pk):
    print(pk)
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
        return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {'form' : form, 'article':article}
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
    
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)