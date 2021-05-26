from accounts.views import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from movies.models import Movie
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required 


#@login_required // 아니면 html에서 저장하기, 프로필로 이동 안 보이게 하고 회원가입, 로그인을 넣는다거나
def index(request):
    person = request.user
    context = {
        'person': person,
    }
    return render(request, 'recommend/index.html', context)


@require_safe
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


@login_required
# @require_POST
def load(request):
    print(request.POST)
    if request.method == 'POST':
    # if request.user.is_authenticated:
        user = request.user
        user.personal_color = request.POST.get('personal_color')
        user.color_code = request.POST.get('color_code')
        user.save()
        message = { 'content' : '정상적으로 저장되었습니다.'}
    return JsonResponse(message)


@require_safe
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
