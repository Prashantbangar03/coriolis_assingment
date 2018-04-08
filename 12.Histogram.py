def create_Histogram(number_list):
	for i in number_list:
		for j in range(int(i)):
			print("#",end="")
		print("")






number_list=input("enter the numberds")
number_list=number_list.split(",")
create_Histogram(number_list)