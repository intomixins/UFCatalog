from django.shortcuts import render
from django.views.generic import ListView
from .models import Fighter

MENU = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


# class FightersList(ListView):
#     template_name = 'my_site/index.html'
#     queryset = Fighter.objects.all()
#     extra_context = {
#         'menu': MENU,
#         'posts': queryset
#     }


def index(request):
    posts = Fighter.objects.all()
    return render(request, 'my_site/index.html',
                  {'menu': MENU, 'posts': posts, 'title': 'Main Page'})


def about(request):
    return render(request, 'my_site/about.html')