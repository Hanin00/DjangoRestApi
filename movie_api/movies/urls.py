from django.conf.urls import url,include
 from django.contrib import admin
 from rest_framework import routers
 from movies.views import MovieViewSet

 router = routers.DefaultRouter()
  router.register('movies',MovieViewSet)
URL pattern: ^movies/$ Name: 'movie-list'
URL pattern: ^movies/{pk}/$ Name: 'movie-detail'

