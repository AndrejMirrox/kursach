from .models import News, Category, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} был создан. Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def news_list(request):
    news = News.objects.all().order_by('-published_at')  # Сортировка по дате публикации
    categories = Category.objects.all()
    return render(request, 'news/news_list.html', {'news': news, 'categories': categories})


def news_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news = News.objects.filter(category=category).order_by('-published_at')
    categories = Category.objects.all()
    return render(request, 'news/news_by_category.html', {'category': category, 'news': news, 'categories': categories})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    comments = news_item.comments.all().order_by('-created_at')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # Перенаправление на страницу входа
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.author = request.user
            comment.save()
            return redirect('news:news_detail', news_id=news_id)
    else:
        form = CommentForm()
    return render(request, 'news/news_detail.html', {
        'news_item': news_item,
        'comments': comments,
        'form': form
    })
