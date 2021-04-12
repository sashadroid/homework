x = int(input("Введите число, факториал которого Вы хотите получить: "))
u = 1
for i in range(1, x+1):
	u *= i
print(u)
