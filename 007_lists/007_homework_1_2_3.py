# Задание 1

list = [8, 16, 0, 4, -23, 9]
ma = max(list[0::])
print(" Наибольший элемент списка = ", ma)
mi = min(list[0::])
print(" Наименьший элемент списка = ", mi)
x = sum(list[0::])
print(" Сумма всех элементов списка = ", x)
y = x/len(list)
print(" Средняя арифметическая элементов списка = ", y)

# Задание 2

stup = 5
l = [1, 2]
for i in range(stup - 2):
	l.append(l[i]+l[i+1])
print(" Количество способов подняться на требуемую ступень = ", l)

# Задание 3


line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
simple_list = []
for i in line:
    simple = True
    if i == 1:
        simple = False
    for y in range(2, i):
        if (i % y == 0):
            simple = False
    if simple == True:
        simple_list.append(i)
        print(i)
x = input("Вы хотите сложить или умножить данные числа?(Да/Нет) ")
if x == "Нет":
    print("Ну ладно, давай тогда.")
elif x == "Да":
    z = input("Для умножения введите (*), для сложения введите (+): ")
    if z == "+":
        s = sum(simple_list[0::])
        print("Сумма этих чисел = ", s)
    elif z == "*":
        w = 1
        for f in simple_list:
            w *= f
        print("Произведение этих чисел = ", w)
