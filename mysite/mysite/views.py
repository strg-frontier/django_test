from django.shortcuts import render_to_response
from polls.models import Poll
from django.http import Http404

# Create your views here.

def index(request):
  latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
  return render_to_response('polls/index.html',
    {'latest_poll_list': latest_poll_list})

def detail(request,poll_id):
  try:
    p = Poll.objects.get(id=poll_id)
  except Poll.DoesNotExist:
    raise Http404
  return render_to_response('polls/detail.html',{'poll':p})
