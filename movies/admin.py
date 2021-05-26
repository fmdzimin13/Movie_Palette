from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'release_date', 'custom_genre',]


admin.site.register(Movie, MovieAdmin)