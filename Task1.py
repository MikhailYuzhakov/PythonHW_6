# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

print("Введите выражение (каждый знак и число отделяется пробелом): ")
equ = input()
print("Eval =", eval(equ))
equ = equ.replace('+', ' + ')
equ = equ.replace('-', ' - ')
equ = equ.replace('*', ' * ')
equ = equ.replace('/', ' / ')
equ = equ.split()

i = 0
N = len(equ)

while (len(equ) > 1):
    while (i < (len(equ) - 1)):
        if (equ[i] == '*'):
            equ[i] = float(equ[i-1]) * float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
        i = i + 1

    i = 0
    while (i < (len(equ) - 1)):
        if (equ[i] == '/'):
            equ[i] = float(equ[i-1]) / float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
        i = i + 1

    i = 0
    while (i < (len(equ) - 1)):
        if (equ[i] == '+'):
            equ[i] = float(equ[i-1]) + float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
        i = i + 1
        
    i = 0
    while (i < (len(equ) - 1)):
        if (equ[i] == '-'):
            equ[i] = float(equ[i-1]) - float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
        i = i + 1

print("UserEval =", equ[0])