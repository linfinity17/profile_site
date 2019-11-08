from django.core.management.base import BaseCommand, CommandError
import csv

from nihongo.models import Word

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		Word.objects.all().delete()

		with open('word_list.csv', encoding='utf-8') as f:
			reader = csv.reader(f) 
			for row in reader:
				_, created = Word.objects.get_or_create(
					kanji = row[0],
					kana_reading = row[2],
					meaning = row[1],
					word_type = row[4],
					)
