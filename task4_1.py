print("\nРешение задачи Хороший ребенок.")

print("\nВведите количество наборов (t) данных:")

t = int(input())

for i in range(t):
    
   print("\nВведите количество цифр (n) в наборе данных:")
   
   n = int(input())
   
   print("\nВведите цифры через пробел:")
    
   array = list(map(int, input().split()))
    
   max_multiply = 0
    
   for i in range(n):
            
        temp = array.copy()
            
        temp[i] = min(temp[i] + 1, 9)
               
        multiply = 1
        
        for k in temp:
                
            multiply *= k
                
               
        if multiply > max_multiply:
            
             max_multiply = multiply
    
        print("\nВходные данные:")

        print("t = ", t)

        print("n =", n)

        print(array)

        print("\nВыходные данные:")

        print(f"\nМаксимальное произведение: {max_multiply}")