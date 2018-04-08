def ReverString(string):
	stri=""
	for i in string:
		stri=i+stri
	return stri



def isPallindrom(string):
	strin=ReverString(string)
	if string != strin:
		return "FALSE"
	return "TRUE"


string=input("enter String ")
print(isPallindrom(string))