from nihongo.models import Word
import csv

Word.objects.all().delete()

counter = 1
with open('word_list.csv', encoding='utf-8') as f:
	reader = csv.reader(f) 
	for row in reader:
		_, created = Word.objects.get_or_create(
			word_id = counter,
			kanji = row[0],
			kana_reading = row[2],
			meaning = row[1],
			word_type = row[4],
			)
		counter = counter + 1