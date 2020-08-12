from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Article


class HomePage(View):

    def get(self, request):
        article = Article.objects.all()

        context = {
            'articles': article
        }
        template_name = 'index.html'
        return render(request, template_name, context)


class DetailView(View):
    def get(self, request, title):
        details = get_object_or_404(Article, title=title)
        context = {
            'detail': details
        }
        template_name = 'details.html'
        return render(request, template_name, context)

