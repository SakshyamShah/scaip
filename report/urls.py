
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.get_report, name='get_report'),
	url(r'^new/$', views.report_new, name='report_new'),
	url(r'^thankyou/$', views.thankyou, name='thankyou'),
]