def ReverString(string):
	stri=""
	for i in string:
		stri=i+stri
	return stri

string=input("enter the string ")
print(ReverString(string))