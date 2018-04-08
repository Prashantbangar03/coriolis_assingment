def getlength(word):
	cnt=0
	for i in word:
		cnt=cnt+1
	return cnt


def mapwords(word,number):
	touple=()
	length=getlength(word)
	if length>int(number):
		touple=(word,length)
		list1.append(touple)


words=input("enter the Words ")
number=input("enter the number ")

words=words.split()
list1=[]
for i in words:
	mapwords(i,number)

print(list1)

