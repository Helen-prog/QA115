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

a = [int(input("-> ")) for i in range(int(input("Введите количество элементов цикла: ")))]
s = k = 0
for i in range(len(a)):
    s += a[i]
    if a[i] != 0:
        k += 1
print("Среднее арифметическое:", s / k)
