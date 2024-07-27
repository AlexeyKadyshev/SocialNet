from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = [
    {'title': 'Новости', 'url_name': 'news', 'icon': 'main_topic/icons/news1.png'},
    {'title': 'Мои друзья', 'url_name': 'friends', 'icon': 'main_topic/icons/friend1.png'},
    {'title': 'Мои группы', 'url_name': 'groups', 'icon': 'main_topic/icons/group1.png'},
    {'title': 'Мой профиль', 'url_name': 'profile', 'icon': 'main_topic/icons/profile1.png'},
    {'title': 'Чат', 'url_name': 'chat', 'icon': 'main_topic/icons/chat1.png'},

]


def entrance(request):
    return render(request, 'main_topic/entrance.html')


def index(request):
    data = {
        'page_name': 'Моя локальная социальная сеть',
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'main_topic/index.html', context=data)


def news(request):
    data = {'title': 'Новости',
            'menu': menu,
            'page_name': 'Моя новостная лента'}
    return render(request, 'main_topic/news.html', context=data)


def friends(request):
    data = {'title': 'Друзья',
            'menu': menu,
            'page_name': 'Мои друзья'}
    return render(request, 'main_topic/friends.html', context=data)


def groups(request):
    data = {'title': 'Группы',
            'menu': menu,
            'page_name': 'Мои группы'}
    return render(request, 'main_topic/groups.html', context=data)


def profile(request):
    data = {'title': 'Профиль',
            'menu': menu,
            'page_name': 'Мой профиль'}
    return render(request, 'main_topic/profile.html', context=data)


def chat(request):
    data = {'title': 'Чат',
            'menu': menu,
            'page_name': 'Беседка'}
    return render(request, 'main_topic/chat.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
