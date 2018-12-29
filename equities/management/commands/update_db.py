from django.core.management.base import BaseCommand, CommandError
import requests
import csv
import pandas
import datetime

from equities import models

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		print("Running..")
		today = datetime.date.today()
		start = today - datetime.timedelta(3)

		rows = (today - start).days
		ticker_list = ['RLC','URC','RCI','ROX','BMM','IS','HLCM','GPH','ICT','VLL','EDC','MFC','RWM','DMPL','BLOOM','BRN','TEL','BEL','SM','EW','FLI','CEB','FGEN','GTCAP','CIC','KPH','ANS','OM','FPH','ALCO','EMP','PX','MEG','GLO','FDC','PNX','COL','LAND','CDC','IMI','MRC','ZHI','AC','WEB','GERI','NIKL','DNL','FOOD','LOTO','SPM','BSC','STR','SMC','LIHC','SECB','FYN','PERC','MA','PBC','UBP','ISM','MBT','ION','ATI','ALI','SEVN','LC','MWC','BH','APC','NRCP','PRMX','PSE','CPV','SUN','BDO','ABA','SRDC','PHC','I','CA','MPI','PTC','MED','ACR','GMAP','ROCK','PAX','IRC','CHI','MACAY','EURO','PRC','MER','MHC','SPC','ALHI','PXP','DWC','PNB','SCC','MB','PGOLD','TFHI','DAVIN','PAL','V','SHNG','AEV','SGP','AT','MFIN','AP','MAC','GMA7','CHIB','PHN','SLI','H2O','GSMI','MVC','NI','LTG','MWIDE','PBB','ABS','SMPH','FFI','JGS','REG','TUGS','PIP','RLT','PHA','HOUSE','LSC','PCOR','ABSP','BPI','RCB','COSCO','IMP','JOH','JFC','BLFI','EVER','KEP','PSB','VITA','RRHI','CEI','APO','ARA','SGI','BC','GEO','DIZ','TBGI','VVT','DMC','MARC','MJC','AUB','PPC','LPZ','FAF','WIN','ELI','MJIC','AGI','UNI','COAL','SOC','MG','NOW','FJP','ORE','SFI','ECP','PA','EEI','UPM','FPI','LMG','CIP','OPM','OV','AAA','T','ANI','APX','ACE','IPO','RFM','HI','CPG','VUL','MBC','STN','CSB','PHES','PRIM','AB','WPI','EG','LFM','AR','GREEN','CYBR','LR','CPM','DFNN','2GO','PMPC','STI','CEU','FEU','ATN','BCOR','BHI','CAT','POPI','TFC','VMC','SLF','PLC','MAXS','X','SSI','FNI','JAS','BKR','CNPF','DD','MAH','SBS','CROWN','IDC','MRSGI','IPM','LBC','TECH','NXGEN','SHLPH','HVN','CHP','APL','PIZZA','PHEN','DNA','WLCON','CLI','EAGLE','MRP','FB','SSP','CLC','PPG','FERRO','MGH','PTT','DMW']
		for ticker in ticker_list:
			url = (r'https://quotes.wsj.com/PH/' +
					ticker +
					'/historical-prices/download?MOD_VIEW=page&num_rows=' +
					str(rows) +
					'&range_days=' +
					str(rows) +
					'&startDate=' +
					str(start) +
					'&endDate=' +
					str(today)
				)
			with requests.Session() as s:
			    download = s.get(url)
			    decoded_content = download.content.decode('ISO-8859-1')
			    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
			    df = pandas.DataFrame(list(cr))
			    df.columns = df.iloc[0].str.strip()
			    df = df.drop([0])

			for i in range(1, len(df)+1):
			    obj,created = models.Record.objects.update_or_create(ticker=ticker,
        									tran_date= datetime.datetime.strptime(df['Date'][i],'%m/%d/%y'),
        										defaults={
        											'price_open': float(df['Open'][i]),
        											'price_high': float(df['High'][i]),
        											'price_low': float(df['Low'][i]),
        											'price_close': float(df['Close'][i]),
        											'volume': float(df['Volume'][i]),
        										}
				)
			    print(obj, created)
		url = (r'https://quotes.wsj.com/index/PH/PSEI/historical-prices/download?MOD_VIEW=page&num_rows=' +
					str(rows) +
					'&range_days=' +
					str(rows) +
					'&startDate=' +
					str(start) +
					'&endDate=' +
					str(today)
				)
		with requests.Session() as s:
		    download = s.get(url)
		    decoded_content = download.content.decode('ISO-8859-1')
		    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
		    df = pandas.DataFrame(list(cr))
		    df.columns = df.iloc[0].str.strip()
		    df = df.drop([0])

		for i in range(1, len(df)+1):
		    obj,created = models.Record.objects.update_or_create(ticker='PSEI',
        									tran_date= datetime.datetime.strptime(df['Date'][i],'%m/%d/%y'),
        										defaults={
        											'price_open': float(df['Open'][i]),
        											'price_high': float(df['High'][i]),
        											'price_low': float(df['Low'][i]),
        											'price_close': float(df['Close'][i]),
        											'volume': 0,
        										}
				    )
		    print(obj, created)
