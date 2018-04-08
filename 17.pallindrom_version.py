import string
ignore = string.punctuation + " "
def Reverse(string1):
	string1=string1.lower()
	string2=""
	for i in string1:
		if (i !=" ") and (i not in ignore):
			string2=i+string2
	return string2

def cleanString(string1):
	string2=""
	string1=string1.lower()
	for i in string1:
		if (i !=" ") and (i not in ignore):
			string2=string2+i
	return string2

def is_Palindrome(string1):
	Reverse_string=Reverse(string1)
	clean_string=cleanString(string1)
	#print(Reverse_string+"\t\t")
	#print(clean_string+"\n\n")
	if Reverse_string==clean_string:
		return "Pallindrom"
	else:
		return "Not Pallindrom"
	
	

print (is_Palindrome("Go hang a salami I'm a lasagna hog."))
print (is_Palindrome("Was it a rat I saw?"))
print (is_Palindrome("Step on no pets"))
print (is_Palindrome("Sit on a potato pan, Otis!"))
print (is_Palindrome("Lisa Bonet ate no basil"))
print (is_Palindrome("Satan, oscillate my metallic sonatas"))
print (is_Palindrome("I roamed under it as a tired nude Maori"))
print (is_Palindrome("Rise to vote sir"))
print (is_Palindrome("Dammit, I'm mad!"))
