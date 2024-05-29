from django.shortcuts import render

from .models import Article
def home__page (request):
    article=Article.objects.all()
    return render(request,"index.html",{"article":article})
    