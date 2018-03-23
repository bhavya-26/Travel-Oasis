from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$', views.home_page, name='home_page'),
	url(r'^home/login$', views.login, name='login'),
	url(r'^home/contact_us$', views.contact_us, name='contact_us'),
	url(r'^questions/gender$', views.qgender, name='qgender'),
	url(r'^questions/climate$', views.qclimate, name='qclimate'),
	url(r'^questions/duration$', views.qduration, name='qduration'),
	url(r'^questions/solo$', views.qsolo, name='qsolo'),
]