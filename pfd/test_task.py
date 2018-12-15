from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
import datetime 
import pandas as pd

from equities import models

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		print("Running..")
		url = r"http://wsj.com/mdc/public/page/9_3024-AsianStocks_MANILA.html"

		with Display():
			driver = webdriver.Firefox()
			try:
				driver.get(url)
				html = driver.page_source
				soup = BeautifulSoup(html,'html.parser')
				data = soup.find_all('nobr')


			finally:
				driver.quit()

		i = 0
		row = [data[0].text,]
		database = []

		for item in data:
			if i % 9 != 0:
				row.append(item.text)
			elif i != 0:
				database.append(row)
				row = []
				row.append(item.text)
			i+=1 
		database.append(row)

		df = pd.DataFrame(database)

		today = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%m.%d.%y')
		date_label ="test.csv"

		print(df)

