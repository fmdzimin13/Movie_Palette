from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 창이 뜨자마자 영화 정보를 불러오려면 읽어오는 순서가 중요
    path('get_movies/', views.get_movies, name='get_movies'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<str:username>/', views.profile, name='profile'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
