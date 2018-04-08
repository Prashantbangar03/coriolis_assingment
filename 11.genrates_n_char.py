def genrates_n_char(number,chars):
	stri=""
	for i in range(number):
		stri=stri+chars
	return stri





number=int(input(" enter the number"))
chars=input("enter the character")
print(genrates_n_char(number,chars))