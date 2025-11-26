import math

def user_input():

    print("Задача №1 Спасение утопающего.")

    print("Ввведите 6 значений:")

    d1 = float(input("Введите кратчайшее расстояние (d1) от спасателя до кромки воды (в ярдах):"))

    d2 = float(input("Введите кратчайшее расстояние от утопающего до берега (в футах):"))

    h = float(input("Введите боковое смещение между спасателем и утопающим (в ярдах):"))

    v = float(input("Введите скорость движения спасателя по песку (в милях в час):"))

    n = float(input("Введите коэффициент замедления спасателя при движении в воде:"))

    q = float(input("Введите направление движения спасателя по песку (в градусах):"))
    
    return d1, d2, h, v, n, q
    
def test_user_input():

    print("Тест пользовательского ввода.")
    
    print("d1 > 0:", d1 > 0)
    
    print("d2 > 0:", d2 > 0)
    
    print("h > 0:", h > 0)
    
    print("v > 0:", v > 0)
    
    print("n > 0:", n > 0)
 
def task_calculation(d1, d2, h, v, n, q):

    x = (d1*3) * math.tan(math.radians(q))

    l1 = math.sqrt(math.pow(x, 2) + math.pow((d1*3), 2))

    l2 = math.sqrt(math.pow(((h*3)-x), 2) + math.pow(d2, 2))

    t = (1/(v*5280/3600))*(l1 + (n*l2))
    
    return t, l1, l2
    
def test_task_calculation(t, l1, l2):
    
    print("Тест вычислений программы.")
    
    print("l1 > 0:", l1 > 0)
    
    print("l2 > 0:", l2 > 0)
    
    print("t > 0", t > 0)
    
def calculation_output(q, t):

    print("Вывод ответа:")

    print(f"Если спасатель начнёт движение под углом равным {int(q)} градусам, он достигнет утопащего через {t:.1f} секунд.")
    
def test_calculation_output(t):
    
    print("Тест вывода результатов программы.")
    
    print("t > 0:", t > 0)
    
d1, d2, h, v, n, q = user_input()

test_user_input()

t, l1, l2 = task_calculation(d1, d2, h, v, n, q)

test_task_calculation(t, l1, l2)

calculation_output(q, t)

test_calculation_output(t)
