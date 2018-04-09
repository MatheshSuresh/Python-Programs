def factorial(n):
    factorial=1

    if(n>0):
        for i in range(1,n):
            factorial*=i
    elif(n==0):
        factorial=1
    else:
        print("No factorial for negative value")

    print(factorial)

x=int(input("Enter the number"))
factorial(x)
