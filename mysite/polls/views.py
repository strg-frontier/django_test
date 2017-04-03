from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.html import mark_safe
from .models import Poll
from .models import Choice
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404

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

def vote(request, pk):
  poll = get_object_or_404(Poll,pk=pk)
  try:
    selected_choice = poll.choice_set.get(pk=request.POST['choice'])
  except(KeyError,Choice.DoesNotExist):
    return render(request, 'polls/detail.html',{
      'poll':poll,
      'error_message':"You didn't select a choice",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('poll_results',pk)

def results(request,pk):
  obj = get_object_or_404(Poll,pk=pk)
  return render(request, 'polls/results.html',{
    'poll':obj,
  })
