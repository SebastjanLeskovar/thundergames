from rest_framework import generics, views
from django.contrib.auth.mixins import LoginRequiredMixin

from database.models import Game, MainGenre, Subgenre
from .serializers import GameSerializer, MainGenreSerializer, SubgenreSerializer


class GameListAPIView(LoginRequiredMixin, generics.ListAPIView):
    """API GET request for all Game objects."""

    lookup_field = 'pk'
    serializer_class = GameSerializer

    def get_queryset(self):
        return Game.objects.all()


class GameDetailAPIView(generics.RetrieveAPIView):
    """API GET request for a specific Game object."""

    lookup_field = 'pk'
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class MainGenreListAPIView(LoginRequiredMixin, generics.ListAPIView):
    """API GET request for all MainGenre objects."""

    lookup_field = 'pk'
    serializer_class = MainGenreSerializer

    def get_queryset(self):
        return MainGenre.objects.all()


class MainGenreDetailAPIView(generics.RetrieveAPIView):
    """API GET request for a specific Main genre object."""

    lookup_field = 'pk'
    serializer_class = MainGenreSerializer
    queryset = MainGenre.objects.all()


class SubgenreListAPIView(LoginRequiredMixin, generics.ListAPIView):
    """API GET request for all Subgenre objects."""

    lookup_field = 'pk'
    serializer_class = SubgenreSerializer

    def get_queryset(self):
        return Subgenre.objects.all()


class SubgenreDetailAPIView(generics.RetrieveAPIView):
    """API GET request for a specific Subgenre object."""

    lookup_field = 'pk'
    serializer_class = SubgenreSerializer
    queryset = Subgenre.objects.all()
