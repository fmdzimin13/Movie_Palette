from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recommend'

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'), #post 요청 시도(실패) --> 성공
    path('load_color/', views.load_color, name='load_Color'), #get 요청 시도(성공)
    path('get_movies/', views.get_movies, name='get_movies'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)