# encoding: UTF-8

from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Book
# Create your views here.

def book_list(request):
	"""書籍の一覧"""
	books = Book.objects.all().order_by('id')
	return render(request,
			'cms/book_list.html',
			{'books':books})

def book_edit(request,book_id=None):
	return HttpResponse('書籍の編集')

def book_del(request,book_id):
	return HttpResponse('書籍の削除')
