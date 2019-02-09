from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import MainGenre, SubGenre, Game

### Index ###

class IndexView(ListView):
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


### Game ###

class GameListView(ListView):
    """Return a list of all Game objects."""
    template_name = 'database/game_list.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class GameDetailView(DetailView):
    """Return a datail page of the specific Game object."""
    model = Game
    template_name = 'database/game_detail.html'


class GameAddView(CreateView):
    """Create a new Game object."""
    model = Game
    fields = ['name', 'main_genre', 'subgenres', 'image']
    template_name_suffix = '_add'


class GameEditView(UpdateView):
    model = Game
    fields = ['name', 'main_genre', 'subgenres', 'image']
    template_name_suffix = '_edit'


class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('database:list-game')


### Main genre ###

class MainGenreListView(ListView):
    """Return a list of all MainGenre objects."""
    template_name = 'database/main_genre_list.html'
    context_object_name = 'all_main_genres'

    def get_queryset(self):
        return MainGenre.objects.all()


class MainGenreDetailView(DetailView):
    """Return a datail page of the specific MainGenre object."""
    model = MainGenre
    template_name = 'database/main_genre_detail.html'


class MainGenreAddView(CreateView):
    """Create a new MainGenre object."""
    model = MainGenre
    fields = ['name', 'image']
    template_name_suffix = '_add'


class MainGenreEditView(UpdateView):
    model = MainGenre
    fields = ['name', 'image']
    template_name_suffix = '_edit'


class MainGenreDeleteView(DeleteView):
    model = MainGenre
    success_url = reverse_lazy('database:list-main-genre')


### Subgenre ###

class SubgenreListView(ListView):
    """Return a list of all SubGenre objects."""
    template_name = 'database/subgenre_list.html'
    context_object_name = 'all_subgenres'

    def get_queryset(self):
        return SubGenre.objects.all()


class SubgenreDetailView(DetailView):
    """Return a datail page of the specific Subgenre object."""
    model = SubGenre
    template_name = 'database/subgenre_detail.html'


class SubgenreAddView(CreateView):
    """Create a new Subgenre object."""
    model = SubGenre
    fields = ['name', 'main_genre', 'image']
    template_name_suffix = '_add'


class SubgenreEditView(UpdateView):
    model = SubGenre
    fields = ['name', 'main_genre', 'image']
    template_name_suffix = '_edit'


class SubgenreDeleteView(DeleteView):
    model = SubGenre
    success_url = reverse_lazy('database:list-subgenre')
