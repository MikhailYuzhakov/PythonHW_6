# Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3n+1

print("Введите натуральное N")
N = int(input())

arr = [3*(i+1)+1 for i in range(N)] # используем List comprehension + lambda expression для создания последовательности
listUsr = list(enumerate(arr, 1)) # используем enumerate для создания кортежа
dictUsr = dict(listUsr) # преобразуем кортеж в словарь

print(dictUsr)