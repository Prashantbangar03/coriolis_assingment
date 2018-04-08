def Compute_length(list1):
	cnt=0
	for i in list1:
		cnt=cnt+1
	return cnt



string=input("Enter String OR List")
list1=string.split(',')
length=Compute_length(list1)
print(length)	