vowel=['a','e','i','o','u']
def translate(string):
	stri=""
	for i in string:
		if i not in vowel and i !=' ':
			stri=stri+i+"O"+i 
		else:
			stri=stri+i
	return stri



string=raw_input("enter the string  ")
string=translate(string)
print(string)
