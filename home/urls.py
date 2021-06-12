#from django.contrib import admin
from django.urls import path, include
from home import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('skills.html', views.skills, name='skills'),
    path('blog.html', views.blog, name='blog'),
    path('contact.htm', views.contact, name='contact'),
    path('blog-detail/<slug>' , views.blog_detail , name="blog_detail"),
    path(r'^results/$', views.search, name='search'),
    # path('comment', views.add_comment, name='add_comment'),
]
