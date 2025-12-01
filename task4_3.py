t = int(input())

for _ in range(t):
    
    n, d = map(int, input().split())
    
    number = input().strip()
    
    position = n
    
    for i in range(n):
    
        if int(number[i]) < d:
        
            position = i
            
            break
            
    result = number[:position] + str(d) + number[position:]
    print(result)