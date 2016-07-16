
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.get_report, name='get_report'),
]