from django.contrib import admin
from .models import Category, News, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Какие поля показывать в списке
    search_fields = ('name',)  # Поле для поиска

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'published_at')  # Какие поля показывать
    list_filter = ('category', 'published_at')  # Фильтры по категориям и дате
    search_fields = ('title', 'content')  # Поля для поиска
    ordering = ('-published_at',)  # Сортировка по дате публикации
    date_hierarchy = 'published_at'  # Навигация по датам

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'news', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
