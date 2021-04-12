def sum(s1, s2):
	return s1 + s2
def sub(s1, s2):
	return s1 - s2
def div(s1, s2):
	return s1 / s2
def mul(s1, s2):
	return s1 * s2
name = input("Hi! What is your name? ")
print("Hi", name, "! My name is Calculon! Welcome! I'll help you count the numbers!")
while True:
	oper = input("Please, select one of the operations: +, - , /, *")
	print("You chose", oper, "!")
	s1 = int(input("Write first number!"))
	s2 = int(input("Write second number!"))
	if oper == "+":
		res = sum(s1, s2)
	elif oper == "-":
		res = sub(s1, s2)
	elif oper == "*":
		res = mul(s1, s2)
	elif oper == "/":
		while s2 == 0:
			print("It is not funny, mate!")
			s2 = int(input("Write second number!"))
		else:
			res = div(s1, s2)
	print("You`re result is: ", res, "!", "You`re welcome!")
	yn = input("Please, type (Y/N) if you want to try again!")
	if yn == "N":
		print("\nGood buy!")

