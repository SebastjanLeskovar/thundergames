from django.contrib import admin

from . import models

admin.site.register(models.MainGenre)
admin.site.register(models.Subgenre)
admin.site.register(models.Game)
