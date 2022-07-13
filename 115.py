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

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.0, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Общая прибыль в", m, "=", profit)


# data = ['red', 'green', 'blue']
#
# j = 1
# for i in data:
#     print(j, ") ", i, sep="")
#     j += 1
#
# # for i in range(3):
# #     print(i)
# print()
# for j, i in enumerate(data, 1):
#     print(j, ") ", i, sep="")


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# print(len(b))


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())


# def summa(*param):
#     res = 0
#     for n in param:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6))
# print(summa(3, 4, 5, 6))

# def to_dict(*lst):
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4, 5, 6, 7, 8))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def ch(*args):
#     average = sum(args) / len(args)
#     print("Среднее арифметическое:", average)
#
#     res = []
#     for num in args:
#         if num < average:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 3, 4, 5, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name", student)
#     for i in scores:
#         print(i)
#
#
# print_scores("Jonathan", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 99, 33)
# print_scores("Bob", 3, 5)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def info(**data):
#     for k, v in data.items():
#         print(k, 'is', v)
#     print()
#
#
# info(firstname='Irina', lastname='Sharma', age=22, phone=1234567890)
# info(firstname='Igor', lastname='Wood', email="igor@gmail.com", country='Russia', age=25, phone=7895567890)


# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)


# def func(a, d, *args, radius=0, **kwargs):
#     print(args)
#     return a, d, args, kwargs, radius
#
#
# print(func(1, 2, 3, 4, 5, 6, b=4, c=9, radius=50))

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# print(x | y)
# print({**x, **y})  # {'a': 1, 'b': 3, 'c': 4 }
#
# a = [1, 2, 3]
# print(*a)


# Области видимости (scope)
# локальная
# объемлющая
# глобальная
# внешная


# def hi():
#     # global name
#     name = 'Bob'  # локальная переменная
#     surname = 'Johnson'
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# name = "Tom"  # глобальная переменная
# print(name)
# hi()
# bye()
# # print(surname)

# i = 5
#
#
# def func(arg=i):
#     print(arg, i)
#
#
# i = 6
# func()  # 5 6

# x = 100  # глобальная переменная
#
#
# def func():
#     # x = 50  # объемлющая
#
#     def func1():
#         # x = 10  # локальная переменная
#         return x
#
#     return func1()
#
#
# print(func())


# def add_two(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))


# min = [1, 2, 3]
#
# print(sum(min))
# print(max(min))
# print(min(min))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")

# def func1():
#     a = 6
#
#     def func2(b):
#         # a = 4
#         print(a + b)
#
#     print("Внешняя переменная a =", a)
#     func2(4)
#
#
# func1()

# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(2))
# print(add(7))
#
# one = outer(10)
# print(one(6))
#
# print(outer(5)(2))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res1()
# res2()
# res2()
# res2()
# res2()

# student = {
#     'Alice': 100,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# a = outer(80, 101)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
# print(a(student))
# print(b(student))
# print(c(student))
# print(d(student))

# def calc(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add1 = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = calc(5, 2)
# print(obj1.add1())
#
# obj2 = calc(5, 2)
# print(obj2.sub())
#
# obj3 = calc(5, 2)
# print(obj3.mul())


# lambda-выражения (анонимные функции)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
#
# func1 = lambda x, y: x + y
# print(func1(1, 2))
# print(func1('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# s = lambda a=1, b=2, c=3: a + b + c
#
# print(s())
# print(s(10))
# print(s(10, 20))
# print(s(10, 20, 30))
# print(s(c=20))

# f = lambda *args: args
#
# print(f(1, 2, 3, 4, 5, 6, 7))
# print(f('a', 'b'))

# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = inc(5)
# print(f(2))
#
#
# def inc1(n):
#     return lambda x: x + n
#
#
# f1 = inc1(5)
# print(f1(2))
#
# inc2 = lambda n: lambda x: x + n
#
# f2 = inc2(5)
# print(f2(2))
# print((lambda n: lambda x: x + n)(5)(2))


# print((lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))

# d = {'d': 50, 'a': 20, 'c': 10, 'b': 40}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1], reverse=True)
# print(lst)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[0](12, 3))
# print(a[1](12, 3))
# print(a[2](12, 3))
# print(a[3](12, 3))


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье')),
# }
#
# print(d[7])
# d[7]()

# map(func, *iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.789456, 5.456789, 2.456123, 1.456127, 7.123789, 4.437895]
# print(list(map(round, areas, range(1, 7))))

# s1 = ['a', 'b', 'c', 'd', 'e']
# s2 = [1, 2, 3, 4, 5]
#
# print(dict(map(lambda x, y: (x, y), s1, s2)))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print((list(map(lambda x, y: x + y, l1, l2))))


# filter(func, *iterable)

# t = ('abcd', 'abc', 'adefg', 'dsf', 'dhu')
#
# t2 = tuple(filter(lambda s: len(s) < 4, t))
# # t2 = tuple(map(lambda s: s * 2, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, b)))

# import random
#
#
# listik = [random.randint(1, 40) for i in range(10)]
# print(listik)
# print(list(filter(lambda i: 10 <= i <= 20, listik)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(1, 10)))))

# worlds = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# print(list(filter(lambda word: word == word[::-1], worlds)))
# a = 'tomato'
# print(a[::-1])

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('*' * 30)
#         func()
#         print('*' * 30, end='\n\n')
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print('5 + 2')
#
#
# func_test()
# hello()


# def circle(fn):
#     def wrap():
#         return "(" + fn() + ')'
#
#     return wrap
#
#
# def quard(fn):
#     def wrap():
#         return "<" + fn() + '>'
#
#     return wrap
#
#
# @quard
# @circle
# def func():
#     return '7 + 2'
#
#
# print(func())

# def decor(fn):
#     def wrap(x, y):
#         print('Сумма: ')
#         fn(x, y)
#
#     return wrap
#
#
# @decor
# def func(a, b):
#     print(a + b)
#
#
# func(5, 2)

# def outer(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, '=', end=" ")
#             fn(x, y)
#
#         return wrap
#     return decor
#
#
# @outer('Сумма:', '+')
# def func(a, b):
#     print(a + b)
#
#
# @outer('Разность:', '-')
# def sub(a, b):
#     print(a - b)
#
#
# func(5, 2)
# sub(5, 2)

# def decor(fn):
#     def wrap(*x):
#         print('*' * 30)
#         fn(*x)
#         print('*' * 30, end="\n\n")
#
#     return wrap
#
#
# @decor
# def func(a, b):
#     print(a * b)
#
#
# @decor
# def func1(a, b, c, d):
#     print(a + b + c + d)
#
#
# func(2, 5)
# func1(2, 5, 4, 7)


# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decor
# def print_info(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, end="\n\n")
#
#
# print_info('Борис', 'Елизавета', 'Светлана', study='JavaScript')
# print_info('Владимир', 'Екатерина', 'Виктор')

# def multiply(arg):
#     def middle(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return middle
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# Строки

# print(int('19'))
# print(int(19.5))

# print(int("100", 2))
# print(int("100", 10))
# print(int("100"))
# print(int("100", 8))
# print(int("100", 16))


# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010 + 7)
# print(0o22)
# print(0x12 + 2)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
#
# print('q' in e)

# s = 'Hello'
# # print(s[4:1:-1])
# s = s[:3] + 't' + s[4:]
# print(s)

# print("Привет")
# print(u"Привет")

# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')

# name = 'Дмитрий'
# age = 25
# print("Меня зовут " + name + '. Мне ' + str(age) + ' лет.')
# print("Меня зовут ", name, '. Мне ', age, ' лет.', sep="")
# print(f"Меня зовут {name}. Мне {age * 2} лет.")


# a = 7.45789621
# print(f"Значение числа а = {round(a, 2)}")
# print(f"Значение числа а = {a:.2f}")

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")
# a = 74
# print(f"{{{{{ a }}}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr"home\{dir_name}\{file_name}")


# 'Строка в одинарных кавычках'
#
# '''Строка в тройных одинарных кавычках'''
#
# a = "Строка     в " \
#     "двойных кавычках"
# print(a)
#
# b = """Строка    в
# тройных        двойных
# кавычках"""
# print(b)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('й'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# s = "Test string for me"
# arr = [ord(x) for x in s]
# print(f"ASCII коды: {arr}")
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# print('apple' == 'Apple')
# print('apple' > 'Apple')  # 97 > 65
# print(ord("a"))
# print(ord("A"))

# from random import randint
#
# short = 7
# long = 10
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(short, long)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
#
#
# print("Случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.


# s = "hello, WORLD! I am learning Python."
# print(s.count('l', 4, 18))
# print(s.rindex('l'))
# print(s.index('l'))
#
# print(s.rfind("w"))  # если элемент не найден, возвращает "-1"
# print(s.find("l", 4))


# s = 'один два'
# a = s[s.find(" ") + 1:]
# print(a)
# b = s[: s.find(" ")]
# print(b)
# s = a + " " + b
# print(s)


# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)


# s = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
# s = s[s.find("(") + 1:s.find(")")]
# print(s)

# s = "Using the Hello World guide, you’ll create a repository, start a branch, write comments, and open a pull request."
#
# sym = "U"
# if s.count(sym) == 1:
#     print(s.find(sym))
# elif s.count(sym) >= 2:
#     print(s.find(sym), s.rfind(sym))

# s = '11 23 44 55 23 22'
# s_old = input("Что заменить: ")  # 23
# s_new = input("На что заменить: ")  # !!!
# i = s.find(s_old)
# while i != -1:
#     l = len(s_old)
#     s = s[:i] + s_new + s[i + l:]
#     i = s.find(s_old)
#
# print(s)

# print('py'.center(10))
# print('py'.center(10, '-'))
# print('py'.center(100, '-'))

# print('    py')
# print('    py'.lstrip())
# print('py    '.rstrip())
# print('     py    '.strip())

# print('https://www.python.org/'.strip('htps:/'))
# print('https://www.python.org/'.lstrip('htps:/'))
# print('https://www.python.org/'.rstrip('/'))
# print('https://www.python.org/'.rstrip('.org/').lstrip('/htps:'))

# s = '11 23 44 55 23 22 23 78 23'
# s_old = input("Что заменить: ")  # 23
# s_new = input("На что заменить: ")  # !!!
# print(s.replace(s_old, s_new, 2))

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # a-b-c
#
# print("...".join(['1', '99']))  # 1...99
# print(":".join("Hello"))  # H:e:l:l:o


# print("Строка разделенная пробелами".split())
# print("Строка разделенная пробелами".rsplit())
# print('www.python.org.ru'.split('.', 2))
# print('www.python.org.ru'.rsplit('.', 2))

# a = input("-> ").split()  # -> Hello world
# print(a)  # ['Hello', 'world']


# a = input("Введите ФИО: ").split()
# print(a)
# print(a[0], " ", a[1][0], ". ", a[2][0], ".", sep="")
# print(f"{a[0]} {a[1][0]}. {a[2][0]}.")

# s = "В строке заменить пробелы символом"
# lst = s.split()
# print(lst)
# print('*'.join(lst))
#
# print(s.replace(" ", "*"))


# Регулярные выражения
# import re

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счё_та. [7895-1982] Ne w"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# # # reg = r'[12][0-9][0-9][0-9]'
# # # print(re.findall(reg, s))  # возвращает список с найденными совпадениями
# # # print(re.search(reg, s))  # возвращает первое найденное совпадение
# # # # print(re.search(reg, s).span())
# # # # print(re.search(reg, s).start())
# # # # print(re.search(reg, s).end())
# # # # print(re.search(reg, s).group())
# # #
# # # print(re.split(reg, s))  # возвращает список элементов разделенных по заданному шаблону
# # # print(re.sub(reg, "!", s, 1))  # поиск и замена по шаблону
# print(re.findall(reg, s))

# повторения
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1
# {n} - n повторений
# {m,n} - от m до n включительно
# {m,} - от m до бесконечности
# {,n} - от 0 до n включительно

# \d - одна любая цифра [0-9]
# \w - одна любая буква, цифра, символ подчеркивания [A-zА-я0-9_]
# \s - пробельный символ (табуляция \t, перенос на другую строку \n)

# \D
# \W
# \S

# d = 'Цифры: 7, +17, -42, 0013, 0.3'
# print(re.findall(r'[-+]?[\d.]+', d))

# s1 = '05-03-1987 # Дата рождения'
# print("Дата рождения:", re.sub(r'#.*', '', s1))
# # 05.03.1987
# s1 = '05-03-1987 # Дата рождения'
# s2 = re.sub(r'#.*', '', s1)
# print("Дата рождения: ", re.sub(r'#.*', '', s1))
# print(re.sub(r'-', '.', s2))
# print("Дата рождения:", re.sub(r'-', '.', re.sub(r'#.*', '', s1)))
# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:00."
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# s1 = 'author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831'
# reg1 = r'\w+\s*=\s*[^;]+'
#
# print(re.findall(reg1, s1))

# s1 = "12 сентября 2021 года 4564557788"
# reg1 = r'\d{2,4}'
# print(re.findall(reg1, s1))

# s1 = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg1 = r'\+?7\d{10}'
# print(re.findall(reg1, s1))


# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name)
#
#
# print(validate_name('Python_master'))

# print(re.findall(r'\w+', '12 + й + q'))
# print(re.findall(r'\w+', '12 + й + q', flags=re.ASCII))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счё_та. [7895-1982] Ne w"
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
#
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, flags=re.MULTILINE))
# print(re.findall(r'^\w+', text))
# print(re.findall(r'^\w+', text, flags=re.MULTILINE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# text = "Python (в русском языке встречаются названия пито́н[16] или па́йтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r'\[.*?\]'
# print(re.findall(reg, text))

# s = "Петр и Виталий отлично учатся!"
# reg = f"Петр|Виталий|Ольга"
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# reg = r'(?:int|double)\s*=\s*(\d+[.\w+]*)'
# print(re.findall(reg, s))

# s = 'Word2016, PS6, AI5'
# reg = r'(([a-z]+)(\d*))'
# print(re.findall(reg, s, re.I))

# a = '31-12-2021'  #
# pattern = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))

# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# reg = r'(\d+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# s = '10/23/2021 и 10/24/2021'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))


# s = 'google.com and google.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))  #

# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print("Вызов метода")
#
#
# # Point.y = 300
# p1 = Point()
# p1.x = 100
# p1.y = 50
# p1.set_coords(10, 20)
# # Point.set_coords(p1, 10, 22)
#
# print(p1.x, p1.y)
# # p1.z = 200
# print(p1.__dict__)
# print(Point.__dict__)
# print(type(p1))
# print(id(p1))
# print(id(Point))
# p2 = Point()
# p2.set_coords(400, 500)
# # p2.x = 200
# print(p2.x, p2.y)
# # print(p2.__dict__)

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}"
#               f"\nНомер телефона: {self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.address = address
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#
#     def set_phone(self, tel):  # установить (изменить) номер телефона
#         self.phone = tel
#
#     def get_phone(self):  # получить номер телефона
#         return self.phone
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_phone('77-77-77')
# print(h1.get_phone())
# h1.set_city("Сочи")
# print(h1.get_city())
# h1.print_info()


# class Person:
#     skill = 10  # статические свойства
#     count = 0
#
#     def __init__(self, name, surname):  # динамические свойства
#         self.name = name
#         self.surname = surname
#         Person.count += 1
#         self.n = 45
#
#     def __del__(self):
#         print("Удаление экземпляра класса")
#
#     def print_info(self):
#         print("Данные о сотруднике:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# # del p1
# p1.add_skill(3)
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)
#
# p3 = Person('Ирина', 'Dolgih')
#
# print(Person.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#         print("Численность роботов:", Robot.k)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# # print("Численность роботов:", Robot.k)
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# # print("Численность роботов:", Robot.k)
#
# droid3 = Robot('RR-R2-D2')
# droid3.say_hi()
# # print("Численность роботов:", Robot.k)
# droid4 = Robot('T-C-3PO')
# droid4.say_hi()
# # print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# del droid4
# print("Численность роботов:", Robot.k)


# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_values(x) and Point.__check_values(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def __check_values(s):
#         if isinstance(s, (int, float)):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_values(x) and Point.__check_values(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def set_coords_x(self, x):
#         if Point.__check_values(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.__check_values(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(50, 100.3)
# p1.set_coords_x(300)
# p1.set_coords_y(200)
# print(p1.get_coords())
# print("x =", p1.get_coords_x())
# print("y =", p1.get_coords_y())
# print(p1.__x, p1.__y)
# p1.__x = 100
# p1.__y = 'abc'
# print(p1.x, p1.__y)
# print(p1.__dict__)

# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = "Некорректные данные"
#         self.__year = self.__power = self.__price = 0
#         if Car.__check_value_str(name):
#             self.__name = name
#         if Car.__check_value_str(model):
#             self.__model = model
#         if Car.__check_value_str(color):
#             self.__color = color
#         if Car.__check_value_int(year):
#             self.__year = year
#         if Car.__check_value_int(power):
#             self.__power = power
#         if Car.__check_value_int(price):
#             self.__price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print("Данные должны быть числом")
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print("Данные должны быть строкой")
#             return False
#         return True
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"""Название модели: {self.__name}
# Год выпуска: {self.__year}
# Производитель: {self.__model}
# Мощность двигателя: {self.__power} л.с.
# Цвет машины: {self.__color}
# Цена: {self.__price}""")
#         print(40 * "=")
#
#     def set_year(self, year):
#         if Car.__check_value_int(year):
#             self.__year = year
#
#     def set_power(self, power):
#         if Car.__check_value_int(power):
#             self.__power = power
#
#     def set_price(self, price):
#         if Car.__check_value_int(price):
#             self.__price = price
#
#     def set_name(self, name):
#         if Car.__check_value_str(name):
#             self.__name = name
#
#     def set_model(self, model):
#         if Car.__check_value_str(model):
#             self.__model = model
#
#     def set_color(self, color):
#         if Car.__check_value_str(color):
#             self.__color = color
#
#     def get_name(self):
#         return self.__name
#
#
# c1 = Car('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)  #
# print(c1._Car__name)
# c1._Car__name = "X2"
# print(c1.__dict__)
# c1.print_info()
# c1.set_year(1999)
# c1.set_power(480)
# c1.set_price(12790000)
# c1.set_name('X9')
# c1.set_model("Renault")
# c1.set_color("black")
# c1.print_info()
# print(c1.get_name())

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coord_x(self):   # get - получить
#         return self.__x
#
#     @coord_x.setter
#     def coord_x(self, x):  # set - установить
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             print("Неверный формат данных")
#
#     # coordX = property(__get_coords_x, __set_coords_x)
#
#
# p1 = Point(5, 10)
# # p1.set_coords_x(30)
# p1.coord_x = 30
# print(p1.coord_x)
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # 13
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(a, b, c, d):
#         mx = a
#         if b < mx:
#             mx = b
#         if c < mx:
#             mx = c
#         if d < mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):  # от 0 до 5
#             fact *= i
#         return fact
#
#     # @staticmethod
#     # def factorial(x):
#     #     if x == 0:
#     #         return 1
#     #     factorial = x * Numbers.factorial(x - 1)
#     #     return factorial
#
#
# print("Максимальное число:", Numbers.max(13, 5, 7, 9))
# print("Минимальное число:", Numbers.min(13, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))  # 1*2*3*4*5

# class Numbers:
#     @staticmethod
#     def max(*args):
#         result = args[0]
#         for i in args:
#             if i > result:
#                 result = i
#
#         return result
#
#
# print(Numbers.max(3, 5, 7, 9))


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def sting_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2021',
#     '01/01/2021',
#     '31.12.2021'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.sting_to_db()
#         print(string_to_db)
#     else:
#         print("Неправильная дата или формат строки с датой")
# date1 = Date.from_string('30.12.2021')
# print(date1.sting_to_db())
# date2 = Date.from_string('21/10/2021')
# print(date2.sting_to_db())

# string_date = '23.10.2021'
# day, month, year = map(int, string_date.split("."))  # [23, 10, 2021]
# print(day, month, year)
# date = Date(day, month, year)
# print(date.sting_to_db())
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             # raise TypeError("ФИО должны быть строкой")
#             print("ФИО должны быть строкой")
#             return False
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             # raise TypeError("Неверный формат ФИО")
#             print("Неверный формат ФИО")
#             return False
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 # raise TypeError("В ФИО можно использовать только буквы и дефис")
#                 print("В ФИО можно использовать только буквы и дефис")
#                 return False
#         return True
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             # UserData.__old = 0
#             # raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#             print("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#             return False
#         return True
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 20:
#             # raise TypeError("Вес должен быть веществтенным числом от 20 кг и выше")
#             print("Вес должен быть веществтенным числом от 20 кг и выше")
#             return False
#         return True
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             # raise TypeError("Паспорт должен быть строкой")
#             print("Паспорт должен быть строкой")
#             return False
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             # raise TypeError("Неверный формат паспорта")
#             print("Неверный формат паспорта")
#             return False
#         for p in s:
#             if not p.isdigit():
#                 # raise TypeError("Серия и номер паспорта должны быть числами")
#                 print("Серия и номер паспорта должны быть числами")
#                 return False
#         return True
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         if self.verify_fio(fio):
#             self.__fio = fio
#         else:
#             self.__fio = "Фамилия Имя Отчество"
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         if self.verify_old(year):
#             self.__old = year
#         else:
#             self.__old = 0
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         if self.verify_weight(weight):
#             self.__weight = weight
#         else:
#             self.__weight = 0.0
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         if self.verify_ps(ps):
#             self.__password = ps
#         else:
#             self.__password = "0000 000000"
#
#
# p1 = UserData("Волков2 Игорь Николаевич", 126, "1234 A67890", 80)
# # p1.fio = "Соболев Игорь Николаевич"
# # print(p1.fio)
# # p1.old = 36
# # p1.weight = 76.2
# # p1.password = '4567 123456'
# print(p1.__dict__)

# f = open("text.txt", mode="r")
# f = open("text.txt", "r")
# f = open("text.txt")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('test.txt', 'r')
# print(f.readlines())
# f.close()


# f = open('test.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# f = open('file.txt', 'w')
# f.write("Hello\nWorld")
# f.close()

# f = open('file2.txt', 'a+')
# f.write("New text.")
# f.read()
# f.close()

# with open('test.txt', 'a+') as f:
#     print(f.write('\n0123456789'))

# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line)

import csv

#
# with open("data.csv") as f:
#     file_reader = csv.reader(f)
#     # print(list(file_reader))
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f'Всего в файле {count} строки.')

# with open("data2.csv") as f:
#     reader = csv.reader(f, delimiter=";")
#     for row in reader:
#         print(row)

# with open("data.csv") as f:
#     field_name = ["Имя", "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, fieldnames=field_name)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"{row['Имя']} - {row['Профессия']} - {row['Год рождения']}")
#         count += 1

# with open("student.csv", "w") as f:
#     writer = csv.writer(f, lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     for row in data:
#         writer.writerow(row)
#
# with open("sw_data_new.csv") as f:
#     print(f.read())

# with open("student1.csv", "w") as f:
#     name = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, lineterminator="\r", fieldnames=name)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Вова", "Возраст": "14"})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dictwriter.csv', 'w') as f:
#     writer = csv.DictWriter(f, lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# from bs4 import BeautifulSoup
# import requests
# import re
#
#
# # f = open('index.html').read()
# # soup = BeautifulSoup(f, 'html.parser')
# # # row = soup.find_all("div", class_="name")
# # # row = soup.find("div", class_="name")
# # # row = soup.find("div", id="whois1")
# # row = soup.find_all("div", class_="row")[1].find("div", class_="name").text
# # print(row)
#
#
# # def get_html(url):
# #     rt = requests.get(url)
# #     return rt.text
# #
# #
# # def get_data(html):
# #     soup = BeautifulSoup(html, "html.parser")
# #     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
# #     return p1
# #
# #
# # def main():
# #     url = "https://ru.wordpress.org/"
# #     print(get_data(get_html(url)))
# #
# #
# # if __name__ == '__main__':
# #     main()
#
# # def get_html(url):
# #     rt = requests.get(url)
# #     return rt.text
# #
# #
# # def refined(s):
# #     res = re.sub(r"\D+", "", s)
# #     return res
# #
# #
# # def write_csv(data):
# #     with open('plugins.csv', 'a') as f:
# #         writer = csv.writer(f, lineterminator="\r")
# #         writer.writerow((data['name'], data['url'], data['rating']))
# #
# #
# # def get_data(html):
# #     soup = BeautifulSoup(html, "html.parser")
# #     p1 = soup.find_all("section", class_="plugin-section")[1]
# #     plugins = p1.find_all('article')
# #     for plugin in plugins:
# #         name = plugin.find("h3").text
# #         url = plugin.find("h3").find("a").get('href')
# #         rating = plugin.find("span", class_="rating-count").find("a").text
# #         r = refined(rating)
# #         data = {'name': name, 'url': url, 'rating': r}
# #         write_csv(data)
# #
# #
# # def main():
# #     url = "https://ru.wordpress.org/plugins/"
# #     get_data(get_html(url))
# #
# #
# # if __name__ == '__main__':
# #     main()
#
# def get_html(url):
#     rt = requests.get(url)
#     return rt.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ""
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ""
#
#         try:
#             active = el.find('span', class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#
#         try:
#             c = el.find('span', class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#
#         data = {
#             "name": name,
#             "url": url,
#             "snippet": snippet,
#             "active": active,
#             "cy": cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 5):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

