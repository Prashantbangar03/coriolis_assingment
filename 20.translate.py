dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
def translate(string):
	words=string.split()
	string=""
	for i in words:
		string=string+dict[i]+" "
	return string
	
print(translate("merry christmas and happy new year"))