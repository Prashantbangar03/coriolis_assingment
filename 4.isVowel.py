Vowel=['a','e','i','o','u']

def isVowel(letter):
	if letter in Vowel:
		return "TRUE"
	else:
		return "FALSE"



letter=input("Enter Letter  ")
return_value=isVowel(letter)
print(return_value)