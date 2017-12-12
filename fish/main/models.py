# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import PIL


class Article(models.Model):  # Модель статья
        text = models.TextField()
        author = models.ForeignKey(User, null=False)


class City(models.Model):  # Модель-Город
	name = models.CharField(max_length=90, unique=True)
	gps_weigth = models.DecimalField(max_digits=10, decimal_places=7)
	gps_length = models.DecimalField(max_digits=10, decimal_places=7)


class Water(models.Model):  # Модель-водоём
	TYPES = (('lake', 'Озеро'),
			('river', 'Река'),
			('sea', 'Море'),
			('mini_lake', 'Пруд'))
	type_of_water = models.CharField(max_length=6, choices=TYPES)
	name = models.CharField(max_length=70, unique=True)
	behind_city = models.ForeignKey(City, null=True)


class Fish(models.Model):  # Модель-Рыба
	type_of_fish = models.CharField(max_length=50, unique=True)
	psychology = models.TextField(max_length=2000)  # Повадки, поведение рыбы
	about = models.TextField(max_length=2000)  # описание
	start_nerest = models.DateField()
	end_nerest = models.DateField()
	food = models.TextField(max_length=300)
	home = models.ManyToManyField(Water)
	default_img = models.ImageField()
	ico_img = models.ImageField()	


class Tackle(models.Model):  # Модель снасть
	name = models.CharField(max_length=120, blank=False)
	model = models.CharField(max_length=120, blank=False)
	
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	articles = models.ManyToManyField(Article)
	def get_absolute_url(self):
		return "/tackle/{}/".format(self.id)
	def __unicode__(self):
		return self.name


class FeedbackToTackle(models.Model):  # Модель отзыв к снасти
	text = models.TextField(max_length=300)
	author = models.ForeignKey(User, null=False)
	

class CommentToArticle(models.Model):  # Модель комментарий к статье
	text = models.CharField(max_length=100)
	author = models.ForeignKey(User, null=True)

