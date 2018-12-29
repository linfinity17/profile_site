from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import forms


from equities import models, forms
# Create your views here.


def home(request):
	return render(request,'equities/home.html')

def stock_list(request):
	form = forms.CompareForm()
	request.POST._mutable = True
	stocks = models.Stock.objects.all().order_by('name')
	if request.method == 'POST':
		form = forms.CompareForm(request.POST)
		if form.is_valid():
			stock_list = [form.cleaned_data['stock_1'],
				form.cleaned_data['stock_2'],
				form.cleaned_data['stock_3'],
				form.cleaned_data['stock_4'],
				form.cleaned_data['stock_5']
			]

			compared_stocks = {}
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']
			counter = 1

			for item in stock_list:
				key = 'stock_' + str(counter)
				compared_stocks[key] = models.Record.objects.filter(ticker=item,tran_date__range=[start_date,end_date]).order_by('tran_date')
				counter	+= 1

			return render(request, 'equities/stock_comparison.html',{
				'form':form,
				'stocks':stocks,
				'stock_list':stock_list, 
				'stock_1':compared_stocks['stock_1'],
				'stock_2':compared_stocks['stock_2'],
				'stock_3':compared_stocks['stock_3'],
				'stock_4':compared_stocks['stock_4'],
				'stock_5':compared_stocks['stock_5'],
				})

	return render(request, 'equities/stock_comparison.html',{'form':form, 'stocks':stocks})


def financial_history(request,ticker):
	income_statement = models.IncomeStatementRecord.objects.filter(ticker=ticker.upper()).order_by('date')
	balance_sheet = models.BalanceSheetRecord.objects.filter(ticker=ticker.upper()).order_by('date')
	financial_ratios = models.FinancialRatioRecord.objects.filter(ticker=ticker.upper()).order_by('date')
	is_attr_list = []
	bs_attr_list = []
	fr_attr_list = []
	for item in income_statement[0].__dict__:
		is_attr_list.append(item)
	for item in balance_sheet[0].__dict__:
		bs_attr_list.append(item)
	for item in financial_ratios[0].__dict__:
		fr_attr_list.append(item)
	date_list = []
	for item in income_statement:
		date_list.append(item.date)
	return render(request,'equities/financial_history.html',
		{
		'income_statement':income_statement,
		'ticker':ticker,
		'date_list':date_list[::-1],
		'is_attr_list':is_attr_list[6:],
		'bs_attr_list':bs_attr_list[4:],
		'fr_attr_list':fr_attr_list[4:],
		})

def price_data(request):
	form = forms.InquiryForm()
	request.POST._mutable = True
	stocks = models.Stock.objects.all().order_by('name')
	if request.method == 'POST':
		form = forms.InquiryForm(request.POST)
		if form.is_valid():
			form.data['ticker'] = form.data['ticker'].upper()
			ticker = form.cleaned_data['ticker']
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']
			records = models.Record.objects.filter(ticker=ticker.upper(),tran_date__range=[start_date,end_date]).order_by('-tran_date')
			try: 
				stock_name = models.Stock.objects.get(ticker=ticker.upper()).name
			except: 
				stock_name = ''
			selected_stock = {'ticker':ticker.upper(), 'name': stock_name} 
			return render(request, 'equities/price_data.html',{'form':form, 'records':records, 'stocks':stocks, 'selected_stock': selected_stock})

	return render(request, 'equities/price_data.html',{'form':form, 'stocks':stocks})

