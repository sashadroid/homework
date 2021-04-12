def par(x):
	print("При х=", x, "парабола =", x ** 2)
def hip(x):
	if x != 0:
		print("При х=", x, "гипербола =", 1 / x)
	else:
		print("При х=", x, "Так как на 0 делить нельзя, то и функции такой нет.")
def res():
	i = -5.0
	while True:
		par(i)
		hip(i)
		print()
		i += 0.5
		if i == 5.5:
			break
res()
