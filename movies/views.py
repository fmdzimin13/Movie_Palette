from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
import requests
from pprint import pprint
from .models import Movie
from .forms import MovieForm
from django.db.models import Avg


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


# 네이버 api 배우, 감독 정보 추가
client_id = 'vwPIJqyIOemmmfcDFFmi'
client_secret = 'dn5XCPlugY'

header_parms = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

def add_info():
    movies = Movie.objects.all()
    for movie in movies:
        query = movie.title
        url = f'https://openapi.naver.com/v1/search/movie.json?query={query}'
        res = requests.get(url, headers=header_parms)
        data = res.json()
        # pprint(data)
        # print(data.get('items')[0])
        if data.get('items'):
            movie.subtitle = data.get('items')[0].get('subtitle')
            movie.director = data.get('items')[0].get('director')
            movie.actors = data.get('items')[0].get('actor')
            movie.save()


@require_safe
def home(request):
    # 아래 두 코드는 제출 시에 주석 풀기(db제출하니까 주석처리하고 넣어도 되겠다!)
    # load_movie_data()
    # add_info()
    movies1 = Movie.objects.filter(custom_genre=1).values('poster_path')[:3]
    movies2 = Movie.objects.filter(custom_genre=2).values('poster_path')[:3]
    movies3 = Movie.objects.filter(custom_genre=3).values('poster_path')[:3]
    movies4 = Movie.objects.filter(custom_genre=4).values('poster_path')[:3]
    movies5 = Movie.objects.filter(custom_genre=5).values('poster_path')[:3]
    movies6 = Movie.objects.filter(custom_genre=6).values('poster_path')[:3]
    movies7 = Movie.objects.filter(custom_genre=7).values('poster_path')[:3]
    movies8 = Movie.objects.filter(custom_genre=8).values('poster_path')[:3]
    movies9 = Movie.objects.filter(custom_genre=9).values('poster_path')[:3]
    movies10 = Movie.objects.filter(custom_genre=10).values('poster_path')[:3]

    context = {
        'movies1': movies1,
        'movies2': movies2,
        'movies3': movies3,
        'movies4': movies4,
        'movies5': movies5,
        'movies6': movies6,
        'movies7': movies7,
        'movies8': movies8,
        'movies9': movies9,
        'movies10': movies10,
    }
    return render(request, 'movies/home.html', context)


@require_safe
def index(request):
    movies1 = Movie.objects.filter(custom_genre=1).values('poster_path')[:3]
    movies2 = Movie.objects.filter(custom_genre=2).values('poster_path')[:3]
    movies3 = Movie.objects.filter(custom_genre=3).values('poster_path')[:3]
    movies4 = Movie.objects.filter(custom_genre=4).values('poster_path')[:3]
    movies5 = Movie.objects.filter(custom_genre=5).values('poster_path')[:3]
    movies6 = Movie.objects.filter(custom_genre=6).values('poster_path')[:3]
    movies7 = Movie.objects.filter(custom_genre=7).values('poster_path')[:3]
    movies8 = Movie.objects.filter(custom_genre=8).values('poster_path')[:3]
    movies9 = Movie.objects.filter(custom_genre=9).values('poster_path')[:3]
    movies10 = Movie.objects.filter(custom_genre=10).values('poster_path')[:3]

    context = {
        'movies1': movies1,
        'movies2': movies2,
        'movies3': movies3,
        'movies4': movies4,
        'movies5': movies5,
        'movies6': movies6,
        'movies7': movies7,
        'movies8': movies8,
        'movies9': movies9,
        'movies10': movies10,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def about(request):
    return render(request, 'movies/about.html')


@require_safe
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


@require_safe
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    avg_rank = movie.review_set.aggregate(Avg('rank'))['rank__avg']
    drop = 'https://image.tmdb.org/t/p/w300/'+ movie.backdrop_path
    context = {
        'movie': movie,
        'avg_rank': avg_rank,
        'drop': drop,
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
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/wordcloud_upload.html', context)

    
@require_safe
def search(request):
    keyword = request.GET.get('keyword')
    movies = Movie.objects.search(movie=keyword)
    context = {
        'keyword': keyword,
        'movies': movies, 
    }
    return render(request, 'movies/search_result.html', context)


@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like.filter(pk=user.pk).exists():
            movie.like.remove(user)
            liked = False
        else:
            movie.like.add(user)
            liked = True

        liked_status = {
            'liked': liked,
            'likeCount': movie.like.count()
        }
        return JsonResponse(liked_status)
    return HttpResponse(status=401) #아니면 로그인으로 리다이렉트



def get_movie(request):
    movie_pk = request.GET.get('moviepk')
    movie = get_object_or_404(Movie, pk=movie_pk)
    query = movie.title + ' ' + 'movie trailer'
    print(query)
    context = {'query': query}
    return JsonResponse(context)
