from random import randrange
import re

def brackets(n):
	i, result, brackets = 0, '', '[]'

	while i < n*2:
		result += brackets[randrange(len(brackets))]
		i+=1

	
	bracket_string = result

	while len(re.findall('\[\]', result)) > 0:
		result = re.sub(r'\[\]', '', result)

	if len(result) > 0:
		print bracket_string, 'NOT OK'
	else:
		print bracket_string, 'OK'


brackets(4)
