# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input("Введите число N: "))
k=0
m=0
while ((2**k)<=n):
    m=2**k
    print(m)
    k+=1