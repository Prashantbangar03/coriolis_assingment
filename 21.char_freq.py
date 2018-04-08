dict={}

def char_frequence(string):
	for i in string:
		if i not in dict:
			dict[i]=1
		else:
			count=dict[i]
			count=count+1
			dict[i]=count

char_frequence("abbabcbdbabdbdbabababcbcbab")
print(dict)