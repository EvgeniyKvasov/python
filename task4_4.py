n = int(input())  

a = list(map(int, input().split()))

zero = True

for num in a:
    
    if num != 0:
        
        zero = False
        
        break

if zero:
    
    print("NO")
    
else:
    
    print("YES")
    
    total_sum = 0
    
    for num in a:
        
        total_sum += num

    if total_sum != 0:
        
        print(1)  
        
        print(1, n)  
    else:
        
        split_index = -1
        
        for i in range(n):
            
            if a[i] != 0:
                
                split_index = i
                
                break
        
        print(2)
        
        print(1, split_index + 1)
        
        print(split_index + 2, n)