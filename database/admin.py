from django.contrib import admin

from . import models

admin.site.register(models.MainGenre)
admin.site.register(models.SubGenre)
admin.site.register(models.Game)
