from django.db import models

# Create your models here.
class Word(models.Model):
	word_id = models.AutoField(primary_key = True)
	kanji = models.CharField(max_length=255, default='')
	kana_reading = models.CharField(max_length=255, null=True)
	meaning = models.CharField(max_length=512, null=True)
	word_type = models.CharField(max_length=255, default='')


	def __str__(self):
		return self.kanji

class GrammarPoint(models.Model):
	grammar_id = models.AutoField(primary_key = True)
	rule = models.CharField(max_length=255, default='')
	sample_sentence = models.CharField(max_length=1024, default='')

	def __str__(self):
		return self.rule