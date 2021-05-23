from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

import requests
from pprint import pprint
from .models import Movie
from .forms import MovieForm


API_URL = 'https://api.themoviedb.org/3'
API_KEY = 'a4f4fe301a6ed6249fc06484ad844067'


def get_url(category='movie', feature='', **kwargs):
    url = f'{API_URL}/{category}/{feature}'
    url += f'?api_key={API_KEY}'

    for k, v in kwargs.items():
        url += f'&{k}={v}'
    return url


def get_movie_data(request, custom_genre):
    url = get_url('discover', 'movie', region='KR', language='ko', with_genres=request)
    res = requests.get(url)
 
    for idx, movie in enumerate(res.json().get('results')[:100]):
        if Movie.objects.filter(title=movie.get('title')).count() == 0:
            Movie(
                adult=movie.get('adult'),
                title = movie.get('title'), 
                overview = movie.get('overview'), 
                release_date = movie.get('release_date'),
                vote_average = movie.get('vote_average'),
                poster_path = 'https://image.tmdb.org/t/p/w500'+movie.get('poster_path'),
                backdrop_path = movie.get('backdrop_path'),
                custom_genre = custom_genre,
                ).save()


genre_1 = [10749]
genre_2 = [10751, 16]
genre_3 = [35]
genre_4 = [18]
genre_5 = [99]
genre_6 = [878]
genre_7 = [28, 12, 14]
genre_8 = [27, 53, 9648]
genre_9 = [80, 10752]
genre_10 = [37, 36]
genre_lookup = {1: genre_1, 2: genre_2, 3: genre_3, 4: genre_4, 5: genre_5, 6: genre_6, 7: genre_7, 8: genre_8, 9: genre_9, 10: genre_10}


def load_movie_data():
    for key, value in genre_lookup.items():
        for genre_code in value:
            get_movie_data(genre_code, key)


@require_GET
def home(request):
    # load_movie_data()
    # movies = Movie.objects.all()
    # context = {
    #     'movies': movies,
    # }
    # return render(request, 'movies/index.html', context)
    return render(request, 'movies/home.html')



def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def movie_list(request, custom_genre):
    movies_red = Movie.objects.filter(custom_genre=1)
    movies_orange = Movie.objects.filter(custom_genre=2)
    movies_yellow = Movie.objects.filter(custom_genre=3)
    movies_greenyellow = Movie.objects.filter(custom_genre=4)
    movies_green = Movie.objects.filter(custom_genre=5)
    movies_bluegreen = Movie.objects.filter(custom_genre=6)
    movies_blue = Movie.objects.filter(custom_genre=7)
    movies_darkblue = Movie.objects.filter(custom_genre=8)
    movies_purple = Movie.objects.filter(custom_genre=9)
    movies_redpurple = Movie.objects.filter(custom_genre=10)

    context = {
        'movies_red': movies_red,
        'movies_orange': movies_orange,
        'movies_yellow': movies_yellow,
        'movies_greenyellow': movies_greenyellow,
        'movies_green': movies_green,
        'movies_bluegreen': movies_bluegreen,
        'movies_blue': movies_blue,
        'movies_darkblue': movies_darkblue,
        'movies_purple': movies_purple,
        'movies_redpurple': movies_redpurple,
        'custom_genre': custom_genre,
    }

    return render(request, 'movies/movie_list.html', context)


@require_GET
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movie_detail.html', context)


@require_http_methods(['GET', 'POST'])
def wordcloud_upload(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_list', movie.custom_genre)
    # edit
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/wordcloud_upload.html', context)
