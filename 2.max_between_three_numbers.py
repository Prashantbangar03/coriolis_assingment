def max_between_three_numbers(number1,number2,number3):
		if(number1>number2 and number1> number3):
				return number1
		elif(number2>number3):
				return number2
		else:
				return number3



number1=int(input("Enter first number  "))
number2=int(input("Enter Second Number  "))
number3=int(input("Enter third number  "))

number=max_between_three_numbers(number1,number2,number3)
print (number)