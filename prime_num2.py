n = int(input("Enter a number: "))
prime_num = [ ]
sayac = 0
for i in range(2, n+1) :      
    sayac = 0
    for j in range(2,i) :
        if(i%j == 0):                      
            sayac += 1
    if sayac == 0:  
        prime_num.append(i)      
print(prime_num)          
