import math

def ploshadkruga():
    R = float(input("Введите радиус круга: "))
    ploshadkrugaa = R ** 2 * math.pi
    print(ploshadkrugaa)

def perimetrtreugolnika():
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))
    pertreug = a + b + c
    print(pertreug)

def perimecircle():
    R = float(input("Введите радиус круга: "))
    print(R * 2 * math.pi)

def ploshadtreug():
    a = float(input("Введите длину основания треугольника: "))
    b = float(input("Введите высоту треугольника: "))
    S = a * b / 2
    print(S)

print('Привет! Выберите опцию:')
print('1 - Площадь круга')
print('2 - Периметр треугольника')
print('3 - Периметр круга')
print('4 - Площадь треугольника')

vibor = input()

if vibor == '1':
    ploshadkruga()
elif vibor == '2':
    perimetrtreugolnika()
elif vibor == '3':
    perimecircle()
elif vibor == '4':
    ploshadtreug()
else:
    print('Неправильный выбор опции. Пожалуйста, выберите существующий вариант.')