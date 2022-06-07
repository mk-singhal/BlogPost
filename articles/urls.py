from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articleList, name='list'),
    path('create/', views.articleCreate, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articleDetails, name='detail'),
]
