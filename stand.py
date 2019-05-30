#!/usr/bin/env python
# coding: utf-8

#Импорты
import numpy as np

def alg1():
    global maks
    maks = 0 #обнуление локального максимума
    global mini
    mini = 0 #обнуление локального минимума
    ind = np.array([])#объявление массива индексов максимальных элементов
    for i in range(len(rand)): #цикл поиска локальных максимумов
        if maks < rand[i]:
            maks = rand[i]
            ind = i
        elif maks == rand[i]:
            ind = np.append(ind,i)
    p = maks 
    print('Максимальное число в массиве =',p)
    print('Индексы максимальных элементов массива:', ind)


def vvod():
    print('Выберите способ генерации массива чисел: ')
    print('1) Ручной ввод ')
    print('2) Рандомизация')
    inp = int(input())
    global rand #вывод rand в глобальное значение 
    if inp == 1:
        rand = input()
        rand = np.fromstring(rand, dtype=int, sep=',') #перевод инпута в массив нампая
        print('Введный Вами массив чисел:', rand)
    elif inp == 2:
        print('Введите количество чисел в массиве')
        kolvo = int(input())
        rand = np.random.randint(1,100,kolvo)
    print('Ваш массив: ',rand)
    return(rand)


def alg2():
    global maks
    maks = 0 #обнуление локального максимума
    global mini
    mini = max(rand) #объявление максимума локального минимума
    global ind
    ind = int(0)#индекс максимума
    ind2 = np.array([])#объявление массива индексов максимальных элементов
    ind3 = int(0)#индекс минимума
    ind4 = np.array([])#объявление массива индексов минимальных элементов
    for i in range(len(rand)): #цикл поиска локальных максимумов
        if maks < rand[i]:
            maks = rand[i]
            ind = i
        elif maks == rand[i]:
            ind2 = np.append(ind2,i)
    for i in range(len(rand)):
        if mini > rand[i]:
            mini = rand[i]
            ind3 = i
        elif mini == rand[i]:
            ind4 = np.append(ind4,i)
    if len(ind2) > 1:
        print('Количество максимальных элементов в массиве больше одного, выполнение операции невозможно')
    elif len(ind4) > 1:
        print('Количество минимальных элементов в массиве больше одного, выполнение операции невозможно')
    else:
        m = rand[ind]
        rand[ind] = rand[ind3]
        rand[ind3] = m
        print('Обработанный массив: ', rand)

def chc(x):
    if x == 1:
        vvod()
        alg1()
    elif x == 2:
        vvod()
        alg2()
    else:
        print('Вы ввели неверное число, перезапустите программу')
        #chc()
print('Какой алгоритм вы хотите использовать?')
print('1) Вывод максимального значения')
print('2) Поменять местами минимальное и максимальное значения')
check = input()
try:
    check = int(check)
except ValueError:
    print('Вы ввели не числовое значение')
    print('Перезапустите программу')
finally:
    if type(check) is int:
        ch = int(check)
        chc(ch)
