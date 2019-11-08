from django.shortcuts import render

from nihongo import models
# Create your views here.

import random

def home(request):
	grammar = models.GrammarPoint.objects.all()
	grammar_selection = random.sample(list(grammar),1)

	nouns = models.Word.objects.filter(word_type='n').order_by('word_id')
	adjectives = models.Word.objects.filter(word_type='adj').order_by('word_id')
	verbs = models.Word.objects.filter(word_type='v').order_by('word_id')
	expressions = models.Word.objects.filter(word_type='exp').order_by('word_id')
	nouns_selection = random.sample(list(nouns),8)
	adjectives_selection = random.sample(list(adjectives),5)
	verbs_selection = random.sample(list(verbs),8)
	expressions_selection = random.sample(list(expressions),5)
	print(grammar_selection[0].rule)
	return render(request,'nihongo/home.html',{
		'grammar_selection':grammar_selection,
		'nouns_selection':nouns_selection,
		'adjectives_selection':adjectives_selection,
		'verbs_selection':verbs_selection,
		'expressions_selection':expressions_selection,
		})
