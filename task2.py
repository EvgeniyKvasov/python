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
 
def task_calculation(d1, d2, h, v, n, q):

    x = (d1*3) * math.tan(math.radians(q))

    l1 = math.sqrt(math.pow(x, 2) + math.pow((d1*3), 2))

    l2 = math.sqrt(math.pow(((h*3)-x), 2) + math.pow(d2, 2))

    t = (1/(v*5280/3600))*(l1 + (n*l2))
    
    return t
    
def calculation_output(q, t):

    print("Вывод ответа:")

    print(f"Если спасатель начнёт движение под углом равным {int(q)} градусам, он достигнет утопащего через {t:.1f} секунд.")
    
d1, d2, h, v, n, q = user_input()

t = task_calculation(d1, d2, h, v, n, q)

calculation_output(q, t)