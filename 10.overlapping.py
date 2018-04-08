def overlapping(list1,list2):
	for i in list1:
		for j in list2:
			if i==j:
				return "TRUE"
	return "FLASE"




list1=input(" Enter the First List Values   ")
list2=input(" Enter the Second List Values  ")
list1=list1.split(",")
list2=list2.split(",")
print(overlapping(list1,list2))