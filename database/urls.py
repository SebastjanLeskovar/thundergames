from django.urls import path

from . import views

app_name = 'database'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /

    path('games/', views.GameListView.as_view(), name='games'), # games/
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game'), # game/1/

    path('main-genres/', views.MainGenreListView.as_view(), name='main-genres'), # main-genres/
    path('main-genre/<int:pk>/', views.MainGenreDetailView.as_view(), name='main-genre'), # main-genre/1/

    path('subgenres/', views.SubgenreListView.as_view(), name='subgenres'), # subgenres/
    path('subgenre/<int:pk>/', views.SubgenreDetailView.as_view(), name='subgenre'), # subgenre/1/
]
