from django.views import generic

from .models import MainGenre, SubGenre, Game


class IndexView(generic.ListView):
    """Return the Index page."""
    context_object_name = ''
    template_name = 'database/index.html'
    queryset = Game.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_games'] = Game.objects.all()
        context['all_main_genres'] = MainGenre.objects.all()
        context['all_subgenres'] = SubGenre.objects.all()
        return context


class GameListView(generic.ListView):
    """Return a list of all Game objects."""
    template_name = 'database/game_list.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class GameDetailView(generic.DetailView):
    """Return a datail page of the specific Game object."""
    model = Game
    template_name = 'database/game_detail.html'


class MainGenreListView(generic.ListView):
    """Return a list of all MainGenre objects."""
    template_name = 'database/main_genre_list.html'
    context_object_name = 'all_main_genres'

    def get_queryset(self):
        return MainGenre.objects.all()


class MainGenreDetailView(generic.DetailView):
    """Return a datail page of the specific MainGenre object."""
    model = MainGenre
    template_name = 'database/main_genre_detail.html'


class SubgenreListView(generic.ListView):
    """Return a list of all SubGenre objects."""
    template_name = 'database/subgenre_list.html'
    context_object_name = 'all_subgenres'

    def get_queryset(self):
        return SubGenre.objects.all()


class SubgenreDetailView(generic.DetailView):
    """Return a datail page of the specific Subgenre object."""
    model = SubGenre
    template_name = 'database/subgenre_detail.html'
