def make_ing_form(inputWord):
	if inputWord.endswith('ie'):
		inputWord = inputWord.rstrip('ie')
		inputWord = inputWord+'y'+'ing'
	elif inputWord.endswith('e'):
		inputWord = inputWord[:-1]
		inputWord = inputWord+'ing' 
	elif len(inputWord)==3:
		if inputWord[-2] in 'aiou':
			inputWord = inputWord + inputWord[-1] + 'ing'
	else:
		inputWord=inputWord+'ing'
	return str(inputWord)
 
print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('move'))
print(make_ing_form('hug'))
