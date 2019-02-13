from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'map_app/index.html')

def ajax(request):
    import json
    from django.http.response import JsonResponse
    input_ido = request.POST.getlist("ido")
    input_keido = request.POST.getlist("keido")
    # hoge = "Ajax Response: " + input_ido
    response = json.dumps({'ido':input_ido,'keido':input_keido})
    print(response)

    return HttpResponse(response,content_type='application/javascript; charset=UTF-8')