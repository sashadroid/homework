a = int(input("Введите меньшее натуральное число: "))
b = int(input("Введите большее натуральное число: "))
s = 0
for i in range(a, b+1):
	s += i
print("Сумма натуральных чисел в заданном диапазоне = ", s)
