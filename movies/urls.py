from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 데이터가 로드되는 url(처음 접근 시에만)
    path('', views.home, name='home'),
    # 이후에는 해당 url로 redirect 처리
    path('index/', views.index, name='index'),

    # 각 장르에 해당하는 숫자를(1-10) variable routing으로 같이 넘겨주기
    path('movie_list/<int:custom_genre>/', views.movie_list, name='movie_list'),

    # 각 영화 상세 정보
    path('detail/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # 영화 좋아요(담기)
    path('like/<int:movie_pk>/', views.like, name='like'),

    path('wordcloud/<int:movie_pk>/', views.wordcloud_upload, name='wordcloud_upload'),


    # 브랜드 컨셉 확인 url
    # path('about/', views.about, name='about'),
    # path('red/', views.red, name='red'),
]
