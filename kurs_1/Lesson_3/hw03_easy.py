# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for index, value in enumerate(fruits):
    print('{} {:>6}'.format(str(index + 1) + '.', value))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [1, 5, 2, 3, 6]
b = [6, 2, 3, 1]

set_a = set(a)
set_b = set(b)
new_a = set_a - set_b

print(list(new_a))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [1, 5, 7, 4, 6, 7, 9]
b = []
for x in a:
    if x % 2 == 0:
        b.append(x / 4)
    else:
        b.append(x*2)
print(b)