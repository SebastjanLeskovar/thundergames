from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MainGenre, Subgenre, Game


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
        context['all_subgenres'] = Subgenre.objects.all()
        return context


### API ###

class MainAPIView(LoginRequiredMixin, TemplateView):
    """Return basic information on APIs."""

    template_name = 'api/api_main.html'


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


class GameAddView(LoginRequiredMixin, CreateView):
    """Create a new Game object."""

    model = Game
    fields = ['name', 'main_genre', 'subgenres', 'image']
    template_name_suffix = '_add'


class GameEditView(LoginRequiredMixin, UpdateView):
    """Edit a Game object."""

    model = Game
    fields = ['name', 'main_genre', 'subgenres', 'image']
    template_name_suffix = '_edit'


class GameDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a Game object."""

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


class MainGenreAddView(LoginRequiredMixin, CreateView):
    """Create a new MainGenre object."""

    model = MainGenre
    fields = ['name', 'image']
    template_name_suffix = '_add'


class MainGenreEditView(LoginRequiredMixin, UpdateView):
    """Edit a Main genre object."""

    model = MainGenre
    fields = ['name', 'image']
    template_name_suffix = '_edit'


class MainGenreDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a Main genre object."""

    model = MainGenre
    success_url = reverse_lazy('database:list-main-genre')


### Subgenre ###

class SubgenreListView(ListView):
    """Return a list of all Subgenre objects."""

    template_name = 'database/subgenre_list.html'
    context_object_name = 'all_subgenres'

    def get_queryset(self):
        return Subgenre.objects.all()


class SubgenreDetailView(DetailView):
    """Return a datail page of the specific Subgenre object."""

    model = Subgenre
    template_name = 'database/subgenre_detail.html'


class SubgenreAddView(LoginRequiredMixin, CreateView):
    """Create a new Subgenre object."""

    model = Subgenre
    fields = ['name', 'main_genre', 'image']
    template_name_suffix = '_add'


class SubgenreEditView(LoginRequiredMixin, UpdateView):
    """Edit a Subgenre object."""

    model = Subgenre
    fields = ['name', 'main_genre', 'image']
    template_name_suffix = '_edit'


class SubgenreDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a Subgenre object."""

    model = Subgenre
    success_url = reverse_lazy('database:list-subgenre')


class ContactView(LoginRequiredMixin, TemplateView):
    """Contact information."""

    template_name = 'database/contact.html'
