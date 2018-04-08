def isMember(list1,value):
	for i in list1:
		if i == value:
			return "TRUE"
	return "FALSE"








list1=input("entr the list values with ,   ")
list1=list1.split(",")
value=input("entr the value ")
print(isMember(list1,value))