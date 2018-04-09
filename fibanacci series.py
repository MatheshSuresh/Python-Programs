def fibanacci_series(x):
    a=0
    b=1
    print(a,b)
    for i in range(1,x):
        next=a+b
        a=b
        b=next
        print(next)

n=int(input("Enter the number"))
fibanacci_series(n)