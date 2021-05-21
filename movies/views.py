from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

import requests
from pprint import pprint
from .models import Movie


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
 
    for idx, movie in enumerate(res.json().get('results')[:20]):
        # if Movie.objects.filter(title=movie.get('title')).count() == 0:
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


genre_1 = [18]
genre_2 = [14, 878]
genre_3 = [16]
genre_4 = [28, 12]
genre_5 = [27, 9648, 53]
genre_6 = [80, 10752]
genre_7 = [10749]
genre_8 = [37, 36]
genre_9 = [99]
genre_10 = [10751, 35]
genre_lookup = {1: genre_1, 2: genre_2, 3: genre_3, 4: genre_4, 5: genre_5, 6: genre_6, 7: genre_8, 8: genre_9, 10: genre_10}


def load_movie_data():
    for key, value in genre_lookup.items():
        for genre_code in value:
            get_movie_data(genre_code, key)




@require_GET
def home(request):
    load_movie_data()
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index2.html', context)
    # return render(request, 'movies/home.html')

