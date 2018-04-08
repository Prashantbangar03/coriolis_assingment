def is_panagram(string):
	alphabets=[]
	string=string.lower()
	for i in string:
		if i not in alphabets and i !=" ":
			alphabets.append(i)
	if len(alphabets)==26:
		return "panagram"
	else:
		return "not panagram"

print(is_panagram("The quick brown fox jumps over the lazy dog"))
