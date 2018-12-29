from django.db import models

# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=10, default='', unique=True)
	name = models.CharField(max_length=255, default='')
	alt_name = models.CharField(max_length=255, null=True)
	sector = models.CharField(max_length=50, default='',null=True)


	def __str__(self):
		return self.ticker


class Record(models.Model):
	ticker = models.CharField(max_length=10, default='')
	tran_date = models.DateField(default='')
	price_open = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
	price_high = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
	price_low = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
	price_close = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
	volume = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)

	class Meta:
		unique_together = ('ticker','tran_date',)


	def __str__(self):
		name = self.ticker + " " + str(self.tran_date)
		return name

class IncomeStatementRecord(models.Model):
	ticker = models.CharField(max_length=10, default='')
	date = models.DateField(default='')
	operating_revenue = models.CharField(max_length=30, default='')
	other_revenue = models.CharField(max_length=30, default='')
	gross_revenue = models.CharField(max_length=30, default='')
	gross_expense = models.CharField(max_length=30, default='')
	non_operating_income = models.CharField(max_length=30, default='')
	non_operating_expense = models.CharField(max_length=30, default='')
	income_loss_before_tax = models.CharField(max_length=30, default='')
	income_tax_expense = models.CharField(max_length=30, default='')
	net_income_after_tax = models.CharField(max_length=30, default='')
	net_income_to_parent = models.CharField(max_length=30, default='')
	eps_basic = models.CharField(max_length=30, default='')
	eps_diluted = models.CharField(max_length=30, default='')


class BalanceSheetRecord(models.Model):
	ticker = models.CharField(max_length=10, default='')
	date = models.DateField(default='')
	current_assets = models.CharField(max_length=30, default='')
	total_assets = models.CharField(max_length=30, default='')
	current_liabilites = models.CharField(max_length=30, default='')
	total_liabilities = models.CharField(max_length=30, default='')
	retained_earnings = models.CharField(max_length=30, default='')
	stock_holders_equity = models.CharField(max_length=30, default='')
	equity_parent = models.CharField(max_length=30, default='')
	bvps = models.CharField(max_length=30, default='')


class FinancialRatioRecord(models.Model):
	ticker = models.CharField(max_length=10, default='')
	date = models.DateField(default='')
	current_ratio = models.CharField(max_length=30, default='')
	quick_ratio = models.CharField(max_length=30, default='')
	solvency_ratio = models.CharField(max_length=30, default='')
	debt_ratio = models.CharField(max_length=30, default='')
	de_ratio = models.CharField(max_length=30, default='')
	int_coverage_ratio = models.CharField(max_length=30, default='')
	asset_ratio = models.CharField(max_length=30, default='')
	gross_profit_margin = models.CharField(max_length=30, default='')
	net_profit_margin = models.CharField(max_length=30, default='')
	roa = models.CharField(max_length=30, default='')
	roe = models.CharField(max_length=30, default='')
	pe_ratio = models.CharField(max_length=30, default='')






