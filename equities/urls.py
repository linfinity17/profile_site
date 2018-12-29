from django.urls import path,re_path

from . import views

app_name = 'equities'

urlpatterns = [
	path('',views.home,name='home'),
	path('stocks/',views.stock_list,name='stock_list'),
	path('price_data/',views.price_data,name='price_data'),
	path('stocks/<ticker>',views.financial_history,name='financial_history'),
	
	]