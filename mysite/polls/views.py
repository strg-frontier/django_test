from django.shortcuts import render
from django.utils.html import mark_safe
from .models import Poll
from django.shortcuts import Http404

# Create your views here.

def index(request):
  return render(request, 'polls/index.html',{
	'polls': Poll.objects.all(),
 })

def detail(request,pk):
  try:
    obj=Poll.objects.get(pk=pk)
  except Poll.DoesNotExist:
    raise Http404
  return render(request, 'polls/detail.html',{
	'poll' : Poll.objects.get(pk=pk)
  })
