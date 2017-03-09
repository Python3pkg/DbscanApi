
from django.conf.urls import url
from Dbscapi import views
urlpatterns = [
	url(r'^dbsc$', views.dbsc),
]
