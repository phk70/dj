from django.contrib import admin
from django.urls import path, include
from python_blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="main"),
    path("about/", views.about, name="about"),    
    path("blog/", include("python_blog.urls")),    
]
