from django.core.management.base import BaseCommand, CommandError
import csv

from nihongo.models import GrammarPoint

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		GrammarPoint.objects.all().delete()
		with open('grammar_list.csv', encoding='utf-8') as f:
			reader = csv.reader(f) 
			for row in reader:
				_, created = GrammarPoint.objects.get_or_create(
					rule = row[0],
					sample_sentence = row[1],
					)
				print(row)

