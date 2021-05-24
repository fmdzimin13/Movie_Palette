from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from movies.models import Movie
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse


def index(request):
    person = request.user
    context = {
        'person': person,
    }
    return render(request, 'recommend/index.html', context)


def load_color(request):
    print(request.GET)
    personal_color = request.GET.get('name')
    color_code = request.GET.get('code')
    print(personal_color)
    if request.user.is_authenticated:
        user = request.user
        user.personal_color = personal_color
        user.color_code = color_code
        user.save()

        message = { 'content' : '정상적으로 저장되었습니다.'}
    return JsonResponse(message)


@require_POST
def load(request):
    print(request.POST)
    if request.user.is_authenticated:
        user = request.user
        user.personal_color = request.POST.get('personal_color')
        user.color_code = request.POST.get('color_code')
        user.save()
        message = { 'content' : '정상적으로 저장되었습니다.'}
    return JsonResponse(message)


def get_movies(request):
    recommend_genre1 = request.GET.get('target_genre1')
    recommend_genre2 = request.GET.get('target_genre2')
    # print(request.GET)
    # print(recommend_genre1)
    # print(recommend_genre2)
    # movies = Movie.objects.filter(Q(custom_genre=recommend_genre1) | Q(custom_genre=recommend_genre2))[:5].values('poster_path')
    movies = Movie.objects.filter(Q(custom_genre=recommend_genre1) | Q(custom_genre=recommend_genre2)).order_by('vote_average')[:5].values('poster_path')
    print(movies)
    recommend = list(movies)
    return JsonResponse(recommend, safe=False)
