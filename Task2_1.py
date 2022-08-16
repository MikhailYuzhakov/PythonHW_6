# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def findUniq(item): # функция для поиска уникальных элементов
    global listUsr
    i = 0
    for itemUser in listUsr: 
        if (item == itemUser): i += 1
    if (i == 1): 
        return item

print("Введите кол-во элементов в последовательности: ")
N = int(input())

listUsr = [randint(0,15) for i in range(N)] # использование list comprehension - заполняем массив случайными числами
print("Сгенерированный массив: ")
print(listUsr)

uniqList = list(map(findUniq, listUsr)) # используем map - передаем каждый элемент listUser в функцию findUniq и результат записываем в новый массив uniqList
print("Нефильтрованный cписок неповторяющихся элементов:")
print(uniqList)

listUsr = list(filter(lambda x: x != None, uniqList)) # используем filter и lambda - фильтруем все элементы со значением None
print("Фильтрованный список неповторяющихся элементов: ")
print(listUsr)
