from django.conf.urls import url
from main.views import test


urlpatterns = patterns(
	url(r'^home/$', test, name='home'),
	url(r'^popular/$', test, name='popular'),  # популярные снасти
	url(r'^read/$', test, name='read'),  # статьи о рыбалке и т.п. сортировка по новым
	url(r'^add/$', test, name='add'),  # view-шка добавления снасти
	url(r'^signin/$', test, name='signin'),  # авторизация и регистрация
	url(r'^signup/$', test, name='signup')  # выход
)
	
