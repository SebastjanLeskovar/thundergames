from django.urls import path

from . import views

app_name = 'database'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /

    path('api/', views.MainAPIView.as_view(), name='api-main'),    # api/

    path('games/', views.GameListView.as_view(), name='list-game'), # games/
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game'), # game/1/
    # TODO: Replace the <pk> in URL with game name.
    path('game/add/', views.GameAddView.as_view(), name='add-game'), # game/add/
    path('game/<int:pk>/edit/', views.GameEditView.as_view(), name='edit-game'), # game/1/edit/
    path('game/<int:pk>/delete/', views.GameDeleteView.as_view(), name='delete-game'), # game/1/delete/


    path('main-genres/', views.MainGenreListView.as_view(), name='list-main-genre'), # main-genres/
    path('main-genre/<int:pk>/', views.MainGenreDetailView.as_view(), name='main-genre'), # main-genre/1/
    # TODO: Replace the <pk> in URL with main genre name.
    path('main-genre/add/', views.MainGenreAddView.as_view(), name='add-main-genre'), # main-genre/add/
    path('main-genre/<int:pk>/edit/', views.MainGenreEditView.as_view(), name='edit-main-genre'), # main-genre/1/edit/
    path('main-genre/<int:pk>/delete/', views.MainGenreDeleteView.as_view(), name='delete-main-genre'), # main-genre/1/delete/


    path('subgenres/', views.SubgenreListView.as_view(), name='list-subgenre'), # subgenres/
    path('subgenre/<int:pk>/', views.SubgenreDetailView.as_view(), name='subgenre'), # subgenre/1/
    path('subgenre/add/', views.SubgenreAddView.as_view(), name='add-subgenre'), # subgenre/add/
    # TODO: Replace the <pk> in URL with subgenre name.
    path('subgenre/<int:pk>/edit/', views.SubgenreEditView.as_view(), name='edit-subgenre'), # subgenre/1/edit/
    path('subgenre/<int:pk>/delete/', views.SubgenreDeleteView.as_view(), name='delete-subgenre'), # subgenre/1/delete/
]
