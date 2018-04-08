def max_between_two_numbers(number1,number2):
	if number1<number2:
		return number2
	else:
		return number1

number1=int(raw_input("Enter first number first  "))
number2=int(raw_input("Enter Second Number  "))
number=max_between_two_numbers(number1,number2)
print number