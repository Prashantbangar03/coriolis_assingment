def getlength(word):
	cnt=0
	for i in word:
		cnt=cnt+1
	return cnt


def find_longest_word(word):
	longest_word=""
	longest_lenght=0

	for i in word:
		length=getlength(i)
		if(longest_lenght<length):
			longest_lenght=length
			longest_word=i
	return longest_word

words=input("enter the Words ")
words=words.split()
longest_word=find_longest_word(words)
print(longest_word)