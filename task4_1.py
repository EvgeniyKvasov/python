t = int(input())

results = []  

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    max_multiply = 0
    
    for i in range(n):
        temp = array.copy()
        temp[i] = temp[i] + 1
        
        multiply = 1
        for num in temp:
            multiply *= num
        
        if multiply > max_multiply:
            max_multiply = multiply
    
    results.append(max_multiply)  

for result in results:
    print(result)