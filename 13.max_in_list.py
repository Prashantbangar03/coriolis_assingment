def max_in_list(list):
	max=list[0]
	for i in list:
		if max < i:
			max=i
	return max

if __name__ == "__main__":
	numbers=input("enter the numbers ")
	numbers=[int(i) for i in numbers.split()]
	print(max_in_list(numbers))
