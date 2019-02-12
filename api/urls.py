from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('games/', views.GameListAPIView.as_view(), name='api-list-game'),  # api/games/
    path('main-genres/', views.MainGenreListAPIView.as_view(), name='api-list-main-genre'), # api/main-genres/
    path('subgenres/', views.SubgenreListAPIView.as_view(), name='api-list-subgenre'),  # api/subgenres/
    path('game/<int:pk>/', views.GameDetailAPIView.as_view(), name='api-game'), # api/game/1/
    path('main-genre/<int:pk>/', views.MainGenreDetailAPIView.as_view(), name='api-main-genre'), # api/main-genre/1/
    path('subgenre/<int:pk>/', views.SubgenreDetailAPIView.as_view(), name='api-subgenre'), # api/subgenre/1/
]
