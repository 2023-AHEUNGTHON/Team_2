from django.shortcuts import render, redirect
from articles.models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

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