from django.shortcuts import render, HttpResponse

USER_COUNT = 10

def about(request):
    context = {'users_count':USER_COUNT}
    return render(request, 'about.html')

# Create your views here.
def blog_catalog(request):
    return HttpResponse(f'<h1>Блог Каталог</h1>')