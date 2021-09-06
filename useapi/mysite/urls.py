from django.urls import path, include
from . import views

app_name = 'mysite'

urlpatterns=[
    path('', views.index, name = 'index'),
    path('get', views.get_api),
    path('post', views.post_api)
]