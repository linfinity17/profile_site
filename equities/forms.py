from django import forms
from django.core import validators

import datetime

def must_be_empty(value):
	if value:
		raise forms.ValidationError('is not empty')

class InquiryForm(forms.Form):
	ticker = forms.CharField()
	start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(2013,2019)))
	end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(2013,2019)),initial=datetime.date.today())
	honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty",validators=[must_be_empty])


