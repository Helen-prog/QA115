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


m = int(input("Введите номер месяца"))

