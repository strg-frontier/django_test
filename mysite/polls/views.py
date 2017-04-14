from django.shortcuts import render,redirect
from django.utils.html import mark_safe
from django.contrib.auth.decorators import login_required
from .models import Poll
from .models import Choice
from django.shortcuts import Http404,get_object_or_404
from .forms import MyForm

# Create your views here.

@login_required
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
    return redirect('polls:results',pk)

def results(request,pk):
  obj = get_object_or_404(Poll,pk=pk)
  return render(request, 'polls/results.html',{
    'poll':obj,
  })

def form_test(request):
  if request.method == "POST":
    form = MyForm(data=request.POST)
    if form.is_valid():
      pass
  else:
    form = MyForm()
  return render(request, 'polls/form.html',{
    'form': form,
  })
