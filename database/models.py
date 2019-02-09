from django.db import models
from django.urls import reverse

class TimeStampedModel(models.Model):
    """An abstract base class model that provides self-updating 'created' and 'modified' fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class MainGenre(TimeStampedModel):
    """Model to create MainGenre objects."""
    name = models.CharField("Name", max_length=50)
    image = models.ImageField("Image", upload_to='main_genre', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('database:main-genre', kwargs={'pk': self.pk})

class SubGenre(TimeStampedModel):
    """Model to create SubGenre objects."""
    name = models.CharField("Name", max_length=50)
    main_genre = models.ForeignKey(MainGenre, verbose_name="main genre", on_delete=models.SET("Please select main genre."))
    image = models.ImageField("Image", upload_to='subgenre', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('database:subgenre', kwargs={'pk': self.pk})


class Game(TimeStampedModel):
    """Model to create Game objects."""
    name = models.CharField("Name", max_length=50)
    main_genre = models.ForeignKey(MainGenre, verbose_name="main genre", blank=True, on_delete=models.SET("Please select main genre."))
    subgenres = models.ManyToManyField(SubGenre, verbose_name="Subgenre", blank=True)
    image = models.ImageField("Image", upload_to='game', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('database:game', kwargs={'pk': self.pk})
