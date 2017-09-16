# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Article(models.Model):  # Модель статья
        text = models.TextField()
        author = models.ForeignKey(User, null=False)


class Tackle(models.Model):  # Модель снасть
	name = models.CharField(max_length=120, unique=True)
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

