def sumoflist(list1):
	sumn=0
	for i in list1:
		sumn=sumn+i
	return sumn

def muloflist(list1):
	muln=1
	for i in list1:
		muln=muln*i
	return muln


list1=input("enter the numbers list")
list1=map(int,list1)
print("sum of number",sumoflist(list1))
print("multiplication of numbers",muloflist(list1))
