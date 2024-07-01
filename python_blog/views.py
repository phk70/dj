from django.shortcuts import render, HttpResponse


def about(request):
    return HttpResponse(f'<h1>О нас</h1>')

# Create your views here.
def blog_catalog(request):
    return HttpResponse(f'<h1>Блог Каталог</h1>')