name = input("Hi! What is your name? ")
print("Hi", name, "! My name is Calculon! Welcome! I'll help you count the numbers!")
while True:
	oper = input("Please, select one of the operations: +, - , /, *, ^, radical  ")
	print("You chose", oper, "!")
	num1 = int(input("Write first number!"))
	num2 = int(input("Write second number!"))
	if oper == "+":
		res = num1 + num2
	elif oper == "-":
		res = num1 - num2
	elif oper == "*":
		res = num1 * num2
	elif oper == "/":
		if num2 == 0:
			print("It is not funny, mate!")
			num2 = int(input("Write second number!"))
		res = num1 / num2
	elif oper == "^":
		res = num1 ** num2
	elif oper == "radical":
		res = num2 ** (1/num1)
	print("You`re result is: ", res, "!", "You`re welcome!")
	yn = input("Please, type (Y/N) if you want to try again")
	if yn == "N":
		print()
		print("Good buy!")
		break
