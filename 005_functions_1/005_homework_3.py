

def step(n):
	if n == 1 or n == 0:
		return 1
	return step(n - 1) + step(n - 2)
stup = int(input("Введите необходимую ступень: "))
print(step(stup))

