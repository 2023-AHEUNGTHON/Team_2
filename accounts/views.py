from django.shortcuts import redirect, render
from accounts.models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'accounts/index.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'accounts/detail.html', {'article': article})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('accounts:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = {'form' : form}
    return render(request, 'accounts/create.html', context)

def update(request, pk):
    print(pk)
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', pk=article.pk)
        return redirect('accounts:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {'form' : form, 'article':article}
    return render(request, 'accounts/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('accounts:index')
    else:
        return redirect('accounts:detail', article.pk)
