# encoding: UTF-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	name = models.CharField('Title',max_length=255)
	publisher = models.CharField('出版社',max_length=255,blank = True)
	page = models.IntegerField('ページ数',blank=True,default=0)

	def __unicode__(self):
		return self.name

class Impression(models.Model):
	"""感想"""
	book = models.ForeignKey(Book,verbose_name='書籍',related_name='impressions')
	comment = models.TextField('コメント',blank=True)

	def __unicode__(self):
		return self.comment

