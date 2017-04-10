from django.conf.urls import url
from weight import views

urlpatterns = [
	url(r'^show/$', views.show_graph, name='show_graph'),
]
