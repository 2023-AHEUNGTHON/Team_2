from django.shortcuts import render, redirect
from articles.models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    if request.user.is_anonymous:
        return redirect('accounts:login')
    articles = Article.objects.filter(author=request.user.id)
    return render(request, 'articles/index.html', {'articles': articles})


def detail(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
    
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    commnets = Comment.objects.filter(article=pk)
    context = {
        'article' : article,
        'article_link' : f'http://127.0.0.1:8000/articles/{request.user.id}/list',
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
    
# def comments_create(request, pk):
#     article = Article.objects.get(pk=pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.article = article
#         comment.save()
#     return redirect('articles:detail', article.pk)

def article_list(request, pk):
    articles = Article.objects.filter(author=pk)
    return render(request, 'articles/index.html', {'articles': articles})