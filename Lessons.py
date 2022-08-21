# Задание 1. По двум заданным числам проверить является ли одно квадратом второго
#print('Введите первое число')
#a = int(input())
#print('Введите второе число')
#b = int(input())
# if a*a == b:
#    print(f"{b} является квадратом {a}")
# if b*b == a:
#    print(f"{a} является квадратом {b}")
# else:
#    print ("Числа не являются квадратами друг друга")

# Задание 2. Найти максимальное из пяти чисел
#my_list = (1, 2, 3, 4, 5)
# print(max(my_list))

# Задание 3. Вывести на экран числа от -N до N
#print('Введите число')
#n = int(input())
#a = range(-n,n)
# for i in a:
#    print(i)

# Задание 4. Показать первую цифру дробной части числа
#a = 2000.123
#a_string = str(a)
# print(a_string[a_string.find(".")+1])

# Задание 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
#a = 30
# if (a%5 == 0 and a%10 == 0) or (a%15 == 0 and not a % 30 == 0):
# print ("Кратно")

# Задание 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
#a = int(input('Введите число от 0 до 6: '))
# my_dict = {
#    0: "Понедельник",
#    1: "Вторник",
#    2: "Среда",
#    3: "Четверг",
#    4: "Пятница",
#    5: "Суббота",
#    6: "Воскресенье",
# }
# if a == 5 and a == 6:
#    print(f"{my_dict.get(a)} Выходной день")
# else:
#    print(f"{my_dict.get(a)} Не выходной день")

# Задание 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
#x = [True, False]
#y = [True, False]
#z = [True, False]
#count = 0
# for i in x:
# for j in y:
# for g in z:
#count += 1
#print(f"{count} {not (x or y  or z) == (not x and not y and not z)}")

# Задание 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
#print("Введите x")
#x = int(input())
#print("Введите y")
#y = int(input())
# if (x>0) and (y>0):
#    print('I четверть')
# elif (x>0) and (y<0):
#    print('II четверть')
# elif (x<0) and (y<0):
#    print('III четверть')
# elif (x<0) and (y>0):
#    print('IV четверть')
# else:
#    print('Точка лежит на оси')

# Задание 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
#print("Введите номер четверти")
#numOfQuadro = int(input())

# def whichCoords(numOfQuadro):
#   if numOfQuadro == 1:
#      return "От 1 до бесконечности, y = От  1 до бесконесности"
#   if numOfQuadro == 2:
#      return "От 1 до бесконечности, y = От -1 до -бесконесности"
#   if numOfQuadro == 3:
#      return "От -1 до -бесконечности, y = От -1 до -бесконесности"
#   if numOfQuadro == 3:
#      return "От -1 до -бесконечности, y = От 1 до бесконесности"
# print(whichCoords(numOfQuadro))

# Задание 10. Найти расстояние между двумя точками пространства
#import math
#print('Введите координаты первой точки')
#print('x1 =')
#x1 = int(input())
#print('y1 =')
#y1 = int(input())
#print('z1 =')
#z1 = int(input())
#print('x2 =')
#print('Введите координаты второй точки')
#x2 = int(input())
#print('y2 =')
#y2 = int(input())
#print('z2 =')
#z2 = int(input())
#point1 = (x1, y1, z1)
#point2 = (x2, y2, z2)
# def DistanceBetweenPoint(point1, point2):
# return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))
#print(DistanceBetweenPoint(point1, point2))
