from rest_framework import serializers
from database.models import Game, MainGenre, Subgenre

class GameSerializer(serializers.ModelSerializer):
    """JSON conversion and data validation for Game objects."""

    class Meta:
        model = Game
        fields = [
            'pk',
            'name',
            'main_genre',
            'subgenres',
            'image'
        ]


class MainGenreSerializer(serializers.ModelSerializer):
    """JSON conversion and data validation for MainGenre objects."""

    class Meta:
        model = MainGenre
        fields = [
            'pk',
            'name',
            'image'
        ]


class SubgenreSerializer(serializers.ModelSerializer):
    """JSON conversion and data validation for Subgenre objects."""

    class Meta:
        model = Subgenre
        fields = [
            'pk',
            'name',
            'main_genre',
            'image'
        ]
