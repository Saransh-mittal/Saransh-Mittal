l = []
n = int(input("Enter the no. of fibonaci numbers you want : "))
i = 0
j = 1
if n==1 :
    print("[0]")
elif n==2 :
    print("[0,1]")
else :
    l.append(0)
    l.append(1)
    while(n-2):
        l.append(l[i]+l[j])
        i = i+1
        j = j+1
        n = n-1
    print(l)    
