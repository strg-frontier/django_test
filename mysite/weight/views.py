from django.shortcuts import render

from weight.models import Weight
# Create your views here.

def show_graph(request):
	"""show weight as graph"""
	datas = Weight.objects.all().order_by('date')
	return render(request,
			'weight/show_graph.html',
			{'datas':datas})
