from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from .forms import CustomUserCreationForm, LoginForm
from django.http import JsonResponse, HttpResponse




@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# @require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # print(username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
    
    
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                followed = False
            else:
                person.followers.add(user)
                followed = True

        follow_status = {
            'followed': followed,
            'followersCount': person.followers.count(),
            'followingsCount': person.followings.count(),
        }
        # return redirect('accounts:profile', person.username)
        return JsonResponse(follow_status)


@require_safe
def get_movies(request):
    username = request.GET.get('username')
    person = get_object_or_404(get_user_model(), username=username)
    movies = person.like_movies.all().values()
    # print(movies)
    mylike = list(movies)

    return JsonResponse(mylike, safe=False)
