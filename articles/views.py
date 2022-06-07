from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

def articleList(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articleList.html', {'articles': articles})

def articleDetails(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', {'article': article}) #{} is called context

@login_required(login_url = '/accounts/signin/')
def articleCreate(request):

    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #Save article to DB
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('articles:list')

    else:
        form = forms.CreateArticle()

    return render(request, 'articles/articleCreate.html', {'form': form})
