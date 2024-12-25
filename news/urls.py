from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),  # Главная страница со списком новостей
    path('<int:news_id>/', views.news_detail, name='news_detail'),  # Детальная страница новости
    path('category/<int:category_id>/', views.news_by_category, name='news_by_category'),  # Новости по категории
]
