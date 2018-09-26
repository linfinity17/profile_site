from django import template
import markdown2
from django.utils.safestring import mark_safe

from equities import models

register = template.Library()

@register.inclusion_tag('equities/data_table.html')
def data_table(attr,ticker,tab): 
	"""Returns dict of courses as nav pane"""
	if tab == 'IS':
		income_statement = models.IncomeStatementRecord.objects.filter(ticker=ticker.upper()).order_by('-date').values_list(attr,flat=True)
		return {'table':income_statement}

	if tab == 'BS':
		balance_sheet = models.BalanceSheetRecord.objects.filter(ticker=ticker.upper()).order_by('-date').values_list(attr,flat=True)
		return {'table':balance_sheet}

	if tab == 'FR':
		financial_ratios = models.FinancialRatioRecord.objects.filter(ticker=ticker.upper()).order_by('-date').values_list(attr,flat=True)
		return {'table':financial_ratios}
