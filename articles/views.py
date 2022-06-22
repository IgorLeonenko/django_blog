from django.shortcuts import render
from .models import Article

def index(request):
  articles = Article.objects.all().order_by('id')
  return render(request, 'index.html', {'articles': articles})

def show(request, slug):
  article = Article.objects.get(slug=slug)
  return render(request, 'show.html', {'article': article})