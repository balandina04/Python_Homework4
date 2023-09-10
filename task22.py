# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

a = set()
for i in range(n):
    d = int(input(f"Введите элемент {i + 1} первого множества: "))
    a.add(d)

b = set()
for i in range(m):   
    d = int(input(f"Введите элемент {i + 1} второго множества: "))
    b.add(d)
intersection = a.intersection(b)
s = sorted(list(intersection))
print("Числа, которые встречаются в обоих множествах:", s)