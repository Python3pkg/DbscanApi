from django.conf.urls import url
from DbscanApi import views
urlpatterns = [
	url(r'^dbsc$', views.dbsc),
]
