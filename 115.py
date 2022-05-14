# first_name = "Elena"  # инициализация переменной
# print("Hello,", first_name)
# age = 30
# print(age)
#
# print("Меня зовут " + first_name + ". Мне " + str(age) + " лет.")
# print(type(first_name))
# print(type(age))

# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b
# print(a)
# print(id(a))
# print(id(b))

# a = b = c = 1
# # print(a, b, c)
# print("a =", a)
# print("b =", b)
# print("c =", c)

# a, b, c = 5, "Hello", 9.2
# print("a =", a)
# print("b =", b)
# print("c =", c)

# a = 1
# b = 2
# print("a =", a)
# print("b =", b)
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# a, b = b, a
# print("a =", a)
# print("b =", b)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 46545647489674864541456
# b = 0.46545647489674864541456
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print("строка \
# символов")
# print('строка \
# символов')

# print("Документ \"script.py\" находится \rпо адресу: \n\t\tD:\\Python\\project")

# s1 = "Hello"
# s2 = "Python"
# print(s1, s2)  # перечисление переменных
# print(s1 + ", " + s2 + "!\t\t")  # конкатенация строк
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 5)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(2 / 4)
# print(2 // 4)
# print(6 % 4)
# print(6 ** 2)

# a = 3
# b = 7
# c = 5
# # a, b, c = 3, 7, 5
# s = a + b + c
# print("Сумма:", s)
# compose = a * b * c
# print("Произведение:", compose)
# d = s / 3
# print("Среднее арифметическое:", d)

# numbers = 6 + 4 * 5 ** 2 + 7
# print(numbers)
# numbers = (6 + 4) * (5 ** 2 + 7)
# print(numbers)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)


# num = 4321
# print("Исходное число:", num)
# a = num % 10
# # print(a)  # 1
# num = num // 10
# # print(num)  # 432
# b = num % 10
# # print(b)  # 2
# num = num // 10
# # print(num)  # 43
# c = num % 10
# # print(c)  # 3
# num = num // 10
# # print(num)  # 4
# d = num % 10
# # print(d)  # 4
# print("Обратное число: ", a, b, c, d, sep="")
# res = a * 1000 + b * 100 + c * 10 + d
# print("Обратное число:", res)
# f = str(a) + str(b) + str(c) + str(d)
# print("Обратное число:", f)


# int() - преобразование к числовому типу данных
# str() - преобразование к строковому типу данных
# float() - преобразование к вещественному типу данных
# bool() - преобразование к булеву типу данных


# num1 = "2"
# num2 = 3
# # res = int(num1) + num2
# res = num1 + str(num2)
# print(res)

# print(int(3.8))
#
# print(round(3.5))
# print(round(3.8918, 2))

# a = '5.02'
# b = 10
# c = float(a) + b
# print(c)


# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", end=" ==== ", sep="!!!")
# print("Я учу Python.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("name:", name, "\nage:", age)
# print("name:", name)
# print("age:", age)

# name = input("Ваше имя: ")
# age = input("Ваш возраст: ")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")

# num = int(input("Введите число: "))
# power = int(input("Ввведите степень: "))
# # power = int(power)
# # print(type(num))
# # print(type(power))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)


# True - истина, да, 1
# False - ложь, нет, 0
# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)
# print(int(b1))
# print(int(b2))

# print(bool("python"))
# print(bool(" "))
# print(bool(""))  # False
# print(bool(25))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False


# name = None
# print(name)
# name = input("name: ")
# print(name)


# print(7 == 7)
# print(7 == 5 + 2)
# print(7 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)

# print(2 < 10 < 9)
# print(2 * 5 > 7 >= 4 + 12)

# a = 10
# b = 10
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True = True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False = False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False and True = False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False and False = False


# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True = True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False = True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False or True = True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False or False = False


# print(not 9 - 5)
# print(not 7 - 7)


# if условие:
#    тело
# else:
#    тело

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)
# print("Окончание")

# a = 12
# b = 22
# print("a:", a)
# print("b:", b)
# a = a + b  # 1 + 2 = 3
# b = a - b  # 3 - 2 = 1
# a = a - b  # 3 - 1 = 2
# # b = b // b  # 2 // 2 = 1
# # a = a + a  # 1 + 1 = 2
# print("a:", a)
# print("b:", b)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 15
# b = 5
# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if a == b:
#     print("a == b")


# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")

# a = input("Введите первую строну треугольника: ")
# b = input("Введите вторую строну треугольника: ")
# c = input("Введите третью строну треугольника: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# elif a != b or a != c or b != c:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрами): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# m = int(input("Введите номер месяца"))

# month = int(input("Введите месяц (цифрами): "))
# if 1 <= month <= 2 or month == 12:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")
#
#
# m = int(input("Введите номер месяца: "))
# if 1 <= m <= 12:
#     print("Время года - ", end="")
#     if 1 <= m <= 2 or m == 12:
#         print("Зима")
#     if 3 <= m <= 5:
#         print("Весна")
#     if 6 <= m <= 8:
#         print("Лето")
#     if 9 <= m <= 11:
#         print("Осень")
# else:
#     print("Такого года не существует")

# m = int(input("Введите номер месяца (Цифрами): "))
# if (m == 12) or m == 1 or m == 2:
#     print("Зима - ", end="")
#     if m == 12:
#         print("Декабрь")
#     if m == 1:
#         print("Январь")
#     if m == 2:
#         print("Февраль")
#
# elif m == 3 or m == 4 or m == 5:
#     print("Весна - ", end="")
#     if m == 3:
#         print("Март")
#     if m == 4:
#         print("Апрель")
#     if m == 5:
#         print("Май")
# elif m == 6 or m == 7 or m == 8:
#     print("Лето - ", end="")
#     if m == 6:
#         print("Июнь")
#     if m == 7:
#         print("Июль")
#     if m == 8:
#         print("Август")
# elif m == 9 or m == 10 or m == 11:
#     print("Осень - ", end="")
#     if m == 9:
#         print("Сентябрь")
#     if m == 10:
#         print("Октябрь")
#     if m == 11:
#         print("Ноябрь")
# else:
#     print("Такого меяца не существует")

# a, b = 50, 20
# minim = a if a < b else b
# print(minim)
# print("a == b" if a == b else "a > b" if a > b else "b > a")
# if a == b:
#     print("a == b")
# elif a > b:
#     print("a > b")
# else:
#     print("b > a")

# a = 5
# b = 0
# print(a / b)

# try-except
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")
#
# print("Код далее")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# first_num = input("Введите первое число: ")
# second_num = input("Введите второе число: ")
# try:
#     first_num = int(first_num)
#     second_num = int(second_num)
# except ValueError:
#     first_num = str(first_num)
# finally:
#     print(first_num + second_num)

# Циклы
# while - цикл с неопределенным количесвтвом итераций
# for - цикл с заданным количеством итераций

# Итерация - один шаг цикла

# while условие:
#     блок инструкций

# i = 0  # переменная счетчик
# while i < 5:  # условие выхода из цикла
#     print("i =", i)
#     i += 1  # i = i + 1  # изменение счетчика - шаг цикла
# print("Код далее")
#
# j = 1000
# while j > 0:
#     print(j, end=" ")
#     j //= 10


# n = 0
# while n <= 20:
#     print("n =", n)
#     n += 2
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*")
#     i += 1

# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))


# total = 0
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
#
# while a <= b:
#     if a % 2:
#         total += a  # total = total + a
#         print(a, end=" ")
#     a += 1
# print("\nСумма целых нечетных чисел: ", total)

# Необходимо ввести целое число и проверить его на четность

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# break - завершает цикл
# continue - завершает текущую итерацию цикла

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         print("i =", i)
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# result = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     result *= n
# print("Результат:", result)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# for element in collection:
#      тело цикла


# for i in 'Hello!':
#     print(i)

# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'blue':
#     print(i, "color:", color)
#     i += 1


# print(range(12))

# range(start, stop, step)
# range(9) - от 0 до 9
# range(2, 9) - от 2 до 9

# for i in range(0, 100, 10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10


# a = int(input("Введите целое число: "))
# for i in range(1, a):  # от 1 до 9
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите ширина прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i in range(1, h - 1) and j in range(1, w - 1):
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()


# a = [i * 2 for i in "Hello!"]
# print(a)
#
# for i in 'Hello!':
#     print(i * 2)


# Список (list) - упорядоченная изменяемая коллекция объектов произвольных типов данных

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[2])
#
# print(nums[-2])
#
# nums[2] = 256
# print(nums)
# nums[3] += 100
# print(nums)
#
# print("Длина списка:", len(nums))

# s = ["Hello"]
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))

# n = [5, 2] * 6
# print(n)
# n1 = [2, 4, 6, 8]
# n = list(range(2, 10, 2))
# print(n)
# print(n1)
# if n == n1:
#     print("Списки равны")
# else:
#     print("Списки разные")

# выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)


# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# print(c * 2)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)
# a = [7, 8, 9, 4]
#
# a[4] = 5
# print(a)

# a = [input("-> ") for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов цикла: ")))]
# total = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         total += a[i]
# print("Сумма отрицательных элементов:", total)

# a = [1, 2, 3, 4]
# print(a)
#
# for i in range(len(a)):
#     print("индекс: ", i, ", значение: ", a[i], sep="")
#
# for i in a:
#     print(i, end=" ")


# a = [int(input("->")) for i in range(int(input("Введите количество элементов цикла: ")))]
# lenght = len(a)
# total = 0
# for i in range(len(a)):
#     if a[i] == 0:
#         lenght -= 1
#     else:
#         total += a[i]
# middle_diad = total / lenght
# print("Среднее арифметическое:", middle_diad)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов цикла: ")))]
# s = k = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         k += 1
# print("Среднее арифметическое:", s / k)

# Срезы
# список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:5:2])
# print(s[:])
# print(s[1::2])
# print(s[::-1])
# print(s[5:1:-1])
# print(s[10:20])


# s = [1, 2, 3, 4, 5, 6, 7]
# # print(s[:])
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[:1])
# # print(s[-1:])
# # print(s[3:4])
# # print(s[-3:])
# # print(s[-3:1:-1])
# # print(s[2:5])
# # s[1:3] = [0, 0, 0, 0]
# # print(s)
# # s[1:2] = [20]
# # print(s)
# # s[2] = 200
# # print(s)
# # Методы списков
# print(s)
# s.append(99)  # добавляет элемент в конце списка
# print(s)
# s.extend([1, 2, 3])  # добавляет множество элементов в конце списка
# print(s)
# s.insert(1, 100)  # добавляет элемент в заданное место в списке
# print(s)


# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)

# s = []
# n = int(input("Количество элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка.")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
#
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
#
# print(c)

# s = [1, 11, 2, 22, 3, 33, 2, 11]
# # s[3:] = []
# print(s)
# # s.remove(11)  # удаляет заданный элемент из списка
# # print(s)
# # s.remove(4)  # ValueError
# # print(s)
# m = s.pop(3)  # pop() - удаляет последний элемент из списка, pop(3) - удаление по индексу
# print(s)
# print(m)
# # s.clear()  # очищает список
# del s[4]
# print(s)

# s = []
# n = int(input("Количество элементов: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# index = int(input("Введите индекс: "))
# # del s[index]
# s.pop(index)
# print(s)

# s = [1, 11, 2, 22, 11, 3, 33, 2, 11]
# num = s.count(11)  # возвращает количество заданных значений в списке
# print(num)
# ind = s.index(11, 2, -1)  # возвращает положение первого индекса с заданным значением
# print(ind)
# s.reverse()  # переворачивает элементы списка в обратном порядке
# print(s)
# s.sort()   # сортировка списка по возрстанию
# s.sort(reverse=True)   # сортировка списка по убыванию
# print(s)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len, reverse=True)
# print(s)

# Генерация случайных данных

# import random
#
# print(random.random())
#
# print(random.randint(1, 9))
# print(random.randrange(1, 11, 2))

# import random as r
#
# print(r.randint(1, 9))
# print(r.randrange(1, 11, 2))

# from random import randint, randrange


# print(randint(1, 9))
# print(randrange(1, 11, 2))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(choice(city))
# print(choices(city, k=3))
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=2))
# shuffle(s)
# print(s)
#
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))


# mas = [randint(0, 100) for i in range(10)]
# print(mas)

# Функции агрегирования
# lst = [5, 3, 2, 4, 1]
# print("Длина списка:", len(lst))
# print("Минимальное значение:", min(lst))
# print("Максимальное значение:", max(lst))
# print("Сумма:", sum(lst))
#
# print(min(6, 4))
# print(min(['6a', '4a']))
# print(max(5, 9))
# print(len([5, 9]))
# print(sum([5, 2]))


# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# m = max(mas)
# print(m)
# mas.remove(m)
# mas.insert(0, m)
# print(mas)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# m = min(lst)
# print(m)
# # minimum_index = lst.index(m)
# minimum_index = lst.index(min(lst))
# del lst[0:minimum_index]
# print(lst)

# x = list('1a2b5c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)
#
# lst = []
# print(bool(lst))
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")

# import math
#
# num1 = math.sqrt(2)
# num2 = math.ceil(2.18)
# num3 = math.floor(2.99)
#
# print(round(2.18))
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)
# print(round(math.pi, 2))
#
# radius = 4
# print(math.pi * (radius ** 2))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
#
# seconds = time.time()
# print("Секунды с начала эпохи:", seconds)
#
# locale_time = time.ctime()
# print("Местное времы:", locale_time)
#
# res = time.localtime(seconds)
# print(res)
# print(res.tm_year)
#
# print("Сегодня: ", time.strftime("%B %d, %Y"))
# # print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(4545634645)))


# Функции


# def hello(name, word):  # аргументы
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", 'hi')  # парметры
# hello("Ivan", 'hello')

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 1
# y = 7
# get_sum(x, y)
# n = 5
# m = 7
# get_sum(n, m)
# get_sum(2, 5)
# get_sum("abc", 'def')


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", '-')
# symbol(7, 'X', '0')

# def line(lenght, first, second):
#     flag = 0
#     for i in range(lenght):
#         if flag == 0:
#             print(first, end="")
#             flag = 1
#         else:
#             print(second, end="")
#             flag = 0
#     print()
#
#
# line(5, "+", "-")
# line(12, "X", "0")

# def get_sum(a):
#     print("Сумма:")
#     return a
#
#
# x = 'a'
# y = 'b'
# res = get_sum([1, 2, 3, 4, 6])
# print(res)
# print(get_sum(5, 7))


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# m = maximum(9, 16)
# print(m)


# def diad(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print("Результат:", diad(a, b))


# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))

# def change(lst):
#     last = lst.pop()
#     first = lst.pop(0)
#     lst.append(first)
#     lst.insert(0, last)
#     return lst
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(10, 15))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if has_upper and has_lower and has_num and len(password) >= 8:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")  # qW2
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# m = 2
# print(get_sum(1, 5, d=m))


# def funct(count=20, sym='-'):
#     for i in range(count):
#         print(sym, end="")
#     print()
#
#
# funct(7, "+")
# funct()
# funct(10)
# funct(sym="@")

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, "\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23)

# a = 5
# b = 5
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
# print()
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(id(lst1))
# print(id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)

# lst1 = [1, 2, 3]
# print(id(lst1))
# lst1.append(4)
# lst1.pop(1)
# print(lst1)
# print(id(lst1))


# Кортежи (tuple)

# lst = [10, 20, 30]  # изменяемый тип данных
# tpl = (10, 20, 30)  # неизменяемый тип данных
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = (1,)
# print(a)
# print(type(a))
# b = tuple((1,))
# print(b)
# print(type(b))

# t = tuple('hello')
# print(t)
# print(t[1])
# print(t[1:3])

# t[1] = 't'

# s = tuple(int(input('-> ')) for i in range(3))
# print(s)

# s = input("Введите слово: ")
# a = tuple(s)
# print(a)

# from random import randint
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for j in range(10)))

# print(tuple(2 ** i for i in range(1, 13)))

# t1 = tuple('hello')
# t2 = tuple(' world')
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# # print(t3.index('l'))
# # if 'r' in t3:
# #     print(t3.index('r'))
# # else:
# #     print("Такого символа нет")
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def fill_corteg(diap_begin, diap_end):
#     return tuple(randint(diap_begin, diap_end) for i in range(10))
#
#
# first_corteg = fill_corteg(0, 5)
# second_corteg = fill_corteg(-5, 0)
# third_corteg = first_corteg + second_corteg
# print(first_corteg)
# print(second_corteg)
# print(third_corteg)
# print("0 =", third_corteg.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# print(t[4][0])
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# Распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# name, age, married = user
# print(name, age, married)
# print(user[0])
# print(user[1])
# print(user[2])

# a = (1, 8, 3, 4, 8, 8, 9, 2)
# del a
# print(a)


# a = (1, 8, 3, 4, 8, 8, 9, 2)
# print(a)
# b = list(a)
# print(b)
# c = tuple(b)
# print(c)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, 'население =', city_population)

# Множество (set)

# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(type(s))
# print(s)
# print(len(s))

# a = {1, 5}
# print(a)
# print(type(a))
#
# a = set('hello')
# print(a)
# print(type(a))

# s = {x * x for x in range(10) if x % 2 == 0}
# print(s)

# def to_set(elem):
#     s = set(elem)
#     return s, len(s)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# print('green' not in t)
# for i in t:
#     print(i)

# {результат for переменная in коллекция}
# {результат for переменная in коллекция if условие}
# {результат if условие else результат for переменная in коллекция}
# {результат if условие else результат for переменная in коллекция if условие}

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3}
#
# a.add(4)
# print(a)
#
# users = {'Tom', 'Bob'}
# users.add("Anna")
# print(users)
# # user = 'Tom'
# # if user in users:
# #     users.remove(user)
# # users.discard('Alice')
# # users.pop()
# users.clear()
# print(users)


# a = {0, 1, 2, 3, 4}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# # c = a & b
# # a &= b
# # c = a - b
# # a -= b
# c = a >= b
# print(c)
# print(a)

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print("Общими буквами являются:", end=" ")
# for i in a:
#     print(i, end=" ")

# first = set(input("Введите первую строку: "))
# second = set(input("Введите первую строку: "))
# comp = first - second
# for i in comp:
#     print(i)


# s = frozenset([1, 5, 2, 3, 4, 5])
# print(s)


# Словарь (dict)

# a = [1, 2, 3]
# print(a[2])
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 2}
# print(d['three'])
# print(d)

# d = {'one': "abc", 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one="one", two=2)
# print(d1)
# print(type(d1))


# a = ((0, 14), (2, 3), (0, 2))
# print(dict(a))

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 2}
# print(d['two'])
# d['two'] = 22 ** 2
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [1, 2, 3], True: 1}
# print(d)
# # print(d[42][1])
# # del d[(1, 2.3)]
# # print(d)
# # print('one' in d)
# # print(42 in d)
# for key in d:
#     print(key, "=", d[key])


# d = {'x1': 2, 'x2': 3}
# sumer = 1
# if not d:
#     sumer = False
# else:
#     for key in d:
#         sumer *= d[key]
#
# print(sumer)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 15)}
# print(d)
# rem = int(input("Какой элемент исключить: "))  # 3
# del d[rem]  # d[3]
# print(d)


# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [1, 2, 3], True: 1}
# print(len(d))

# capitals = dict()
#
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны " + country + ": " + capitals[country])
#     else:
#         print("В базе нет страны с названием " + country)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         kol = int(input("Количество: "))
#         goods[n][1] = kol
#         price = int(input("Цена: "))
#         goods[n][2] = price
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# d = {'a': 1, 'b': 2, 'c': 3}

# d2 = d.copy()
#
# print(d)
# print(d2)
#
# d['e'] = 7
# d2['b'] = 5
#
# print(d)
# print(d2)

# print(d['e'])
# value = d.get('b', 'FF')
# print(value)

# n = d.items()
# print(n)
# k = d.keys()
# print(k)
# v = d.values()
# print(v)
#
# # for i, j in d.items():
# #     print(i, "->", j)
# a = tuple(d.values())
# print(a)
#
# q = [('a', 1), ('b', 2), ('c', 3), ('b', 9)]
# print(dict(q))

# item = d.pop('b', 5)
# item = d.popitem()
# item = d.setdefault('e', 7)
# print(item)
# print(d)

# d.update([('d', 7), ('b', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # print(z)
# # z.update(y)
# z = y | x
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d['location'] = d.pop('city')
#
# print(d)

# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")


# a_dict = {'четыре': 4, "один": 1, 'два': 2, 'три': 3}
# d = {k: v for k, v in a_dict.items() if v <= 2}
# print(d)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)
#
# print(list(b.items()))

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip()
# d = dict(zip([1, 2, 3, 2], ['one', 'two', 'three', 'four']))
# print(d)
# a = list(zip([1, 2, 3, 2], ['one', 'two', 'three', 'four']))
# print(a)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# # c = [4.0, 5.0, 6.0]
# z = zip(a, b)
# print(list(z))

# d_one = {'name': 'Igor', 'last_name': 'Smith', 'job': 'Manager'}
# d_two = {'name': 'Irina', 'last_name': 'Doe', 'job': 'Consultant'}
#
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# p = [(2, 'two'), (1, 'one'), (3, 'three')]
# a, b = zip(*p)  # распаковка последовательности
# print("a =", a)
# print("b =", b)
#
# d = list(zip(b, a))
# print(d)
# d.sort()
# print(d)

month = ['January', 'February', 'March']
total_sales = [52000.00, 51000.0, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

for sales, costs, m in zip(total_sales, prod_cost, month):
    profit = sales - costs
    print("Общая прибыль в", m, "=", profit)
    