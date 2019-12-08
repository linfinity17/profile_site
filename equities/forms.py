from django import forms
from django.core import validators

import datetime

from . import models

ticker_list = [('','Select Ticker')]
for item in models.Stock.objects.values('ticker'):
	ticker_list.append((item['ticker'],item['ticker']))

def must_be_empty(value):
	if value:
		raise forms.ValidationError('is not empty')

class InquiryForm(forms.Form):
	ticker = forms.ChoiceField(choices=ticker_list)
	start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(2013,2020)))
	end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(2013,2020)),initial=datetime.date.today())
	honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty",validators=[must_be_empty])

class CompareForm(forms.Form):
	stock_1 = forms.ChoiceField(choices=ticker_list,label="Stock 1*")
	stock_2 = forms.ChoiceField(choices=ticker_list,label="Stock 2*")
	stock_3 = forms.ChoiceField(choices=ticker_list,required=False)
	stock_4 = forms.ChoiceField(choices=ticker_list,required=False)
	stock_5 = forms.ChoiceField(choices=ticker_list,required=False)
	start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(2013,2020)))
	end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(2013,2020)),initial=datetime.date.today())



