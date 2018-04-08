def multiplyBy2(number):
	return 2*number

def is_devisibleby2(number):
	return (number%2==0)

def addition(list):
	addi=0;
	for i in list:
		addi=i+addi;
	return addi

def my_map(func,list1):
	ResultList=[]
	for i in list1:
		ResultList.append(func(i))
	return ResultList

def my_filter(func,list):
	ResultList=[]
	for i in list:
		Reslut=func(i)
		if(Reslut):
			ResultList.append(i)
	return ResultList

def my_reduce(func,list):
	return func(list)


list=[10,20,13,43]
ResultList=my_map(multiplyBy2,list)
print "My Map",ResultList
ResultList=my_filter(is_devisibleby2,list)
print "My Filter",ResultList
Result=my_reduce(addition,list)
print "ny Reduce",Result


