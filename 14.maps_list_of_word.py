def getlength(word):
	cnt=0
	for i in word:
		cnt=cnt+1
	return cnt


def mapwords(word):
	touple=()
	length=getlength(word)
	touple=(word,length)
	list1.append(touple)


words=input("enter the Words ")
words=words.split()
list1=[]
for i in words:
	mapwords(i)

print(list1)

