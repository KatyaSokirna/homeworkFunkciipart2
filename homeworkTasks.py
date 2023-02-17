# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве па-
# раметра. Полученный результат возвращается из функции.


def some_multiplication(*args):
    multiplication = 1
    for number in args:
        multiplication = multiplication * number
    return multiplication


print(some_multiplication(1, 2, 3, 4, 5))


# Задание 2
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.


def numbers_min(*args):
    minimum = args[0]
    for number in args:
        if number < minimum:
            minimum = number
    return minimum


print(numbers_min(3, 5, 2, -1, 1, 29, 2))


# Задание 3
# Напишите функцию, определяющую количество про-
# стых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.

def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(simple(42))#False
print(simple(137))#True


def simple_range(a, b):
    l = []
    count = 0
    for i in range(a, b+1):
        if simple(i):
            l.append(i)
            count = count + 1
    print(count)
    return l


print(simple_range(20, 100))

# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.


def numbers_del(a):
    numbers = [2, 1, 0, 2, 7, 8, 2]
    count = 0
    for i in numbers:
        numbers.pop(0)#Удаляет элемент по индексу, возвращая его
        count = i + 1 #выводит число 3, как раз столько и удаляет
    print(count)
    return numbers #выводит удаленные числа


print(numbers_del(0))


# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.


def lists(a, b):
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    c = []
    for i in a and b:
        c = a + b
    return c


print(lists(1, 10))


# Задание 6
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержа-
# щий полученные результаты.

def degree(a):
    d = 2
    for i in range(a):
        n = a ** d #подносит в степень, получается 3 во 2 степени выводит 9
    return n


print(degree(3))


def list_in_degree(*numbers):
    degree_numbers = []
    for number in numbers:
        a = degree(number)
        degree_numbers.append(a)
    return degree_numbers


print(list_in_degree(2, 4, 5))

