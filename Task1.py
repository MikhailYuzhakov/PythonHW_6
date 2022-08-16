# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

print("Введите выражение: ")
equ = input()
print("Eval =", eval(equ))
equ = equ.replace('+', ' + ')
equ = equ.replace('-', ' - ')
equ = equ.replace('*', ' * ')
equ = equ.replace('/', ' / ')
equ = equ.split()

i = 0
N = len(equ)

while (N > 1):
    for i in range(N):
        if (equ[i] == '*'):
            equ[i] = float(equ[i-1]) * float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
            i = 0
            print(equ)
            N = len(equ)

    for i in range(N):
        if (equ[i == '/']):
            equ[i] = float(equ[i-1]) / float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
            print(equ)
            i = 0
            N = len(equ)

    for i in range(N):
        if (equ[i] == '+'):
            equ[i] = float(equ[i-1]) + float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)  
            print(equ)
            i = 0
            N = len(equ)

    for i in range(N):   
        if (equ[i] == '-'):
            equ[i] = float(equ[i-1]) - float(equ[i+1])
            equ.pop(i-1)
            equ.pop(i)
            print(equ)
            i = 0
            N = len(equ)

print("UserEval =", equ[0])

