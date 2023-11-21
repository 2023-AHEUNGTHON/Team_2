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
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('accounts:detail', pk=article.pk)
    else:
        form = ArticleForm()
        context = {'form' : form}
        return render(request, 'accounts/create.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('accounts:detail', pk=article.pk)
    else:
        return render(request, 'accounts/update.html', {'article': article})

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('accounts:index')
    else:
        return redirect('accounts:detail', article.pk)
