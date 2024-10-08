n=int(input("Введите число"))
a=[0,1]
i=1
while(n>a[i]):
    
    a.append(a[i-1]+a[i])
    i+=1
    n-=1
print(a)