from django.shortcuts import render
from django.http import HttpResponse
from .models import Article 


def a_list(request):
    values= Article.objects.all()
    return render(request, 'articles/article_list.html ', {'articles': values})

