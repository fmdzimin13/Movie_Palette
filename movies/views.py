from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_GET
def home(request):
    # movies = Movie.objects.all()
    # context = {
    #     'movies': movies,
    # }
    # return render(request, 'movies/index.html', context)
    return render(request, 'movies/home.html')