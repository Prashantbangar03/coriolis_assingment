import re
from collections import defaultdict
import time
def alternade_finder(file_name):
	with open(file_name, 'r') as f:
		words = re.findall('\w+', f.read())
		
	foundalternades = defaultdict(list)

	for word in words:
		wordlist, smallerwordeven, smallerwordodd = words[:], '', ''
	
		wordlist.remove(word)

		if len(word) > 1:
			for letters in word: 
				letter_pos = word.index(letters)

				if letter_pos % 2 == 0:
					smallerwordeven += letters 
					if smallerwordeven in wordlist and \
					smallerwordeven not in foundalternades[word]:
						foundalternades[word].append(smallerwordeven)

				if letter_pos % 2 != 0:
					smallerwordodd += letters
					if smallerwordodd in wordlist and \
					smallerwordodd not in foundalternades[word]:
						foundalternades[word].append(smallerwordodd)

	for word, alternades in foundalternades.items():
		alt = reduce(lambda x, y: x + y, alternades)
		if sorted(alt) == sorted(word):
			print '"%s": makes %s' % (word, alternades)

print time.time()
alternade_finder('unixdict.txt')
print time.time()