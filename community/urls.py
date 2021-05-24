from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    # 영화 상세 페이지에서 관련 pk를 넘겨주며 리뷰 작성할 수 있도록
    path('<int:movie_pk>/create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:review_pk>/like/', views.like, name='like'),
]
