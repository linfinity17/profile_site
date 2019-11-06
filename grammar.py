import csv

from nihongo.models import GrammarPoint

with open('grammar_list.csv', encoding='utf-8') as f:
	reader = csv.reader(f) 
	for row in reader:
		_, created = GrammarPoint.objects.get_or_create(rule = row[0])
