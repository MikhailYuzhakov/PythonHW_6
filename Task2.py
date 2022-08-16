# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
usrSum = 0

def sumUsr(item): # функция для суммирования элементов на нечетных позициях
    global usrSum
    if (item[0] % 2 == 1):
        usrSum += item[1]
    return item

userList = [randint(1, 101) for i in range(1, 11)] # используем list comprehesion для генерации случайного списка
print(userList)

ustTuple = list(enumerate(userList, start = 1)) # используем enumerate для создания кортежа, где первый элемент каждой пары это индекс соответсвующего элемента
newList = list(map(sumUsr, ustTuple)) # используем map для подсчета суммы элементов, стоящих на нечетных позициях
print("Сумма элементов, стоящих на нечетных позициях =", usrSum)
