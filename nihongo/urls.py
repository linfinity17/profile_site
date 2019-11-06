from django.urls import path,re_path

from . import views

app_name = 'nihongo'

urlpatterns = [
	path('',views.home,name='home'),
	]