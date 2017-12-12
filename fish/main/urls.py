# -*- coding: utf-8 -*-

from django.conf.urls import url
from main.views import test


urlpatterns = [ 
	url(r'^$', test, name='home'),
	url(r'^popular/$', test, name='popular'),  # популярные снасти
	url(r'^read/$', test, name='read'),  # статьи о рыбалке и т.п. сортировка по новым
	url(r'^add/$', test, name='add'),  # view-шка добавления снасти
	url(r'^signin/$', test, name='signin'),  # авторизация и регистрация
	url(r'^signout/$', test, name='signout'),  # выход
	url(r'^tackle/(\d+)/$', test, name='tackle')  # снасть
]
	
