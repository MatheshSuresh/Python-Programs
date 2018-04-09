def prime_number(n):
    value=0
    for i in range(2,int(n/2)):
        if(n%i==0):
            value=1

    if(value==1):
        print("It not a is prime number")
    else:
        print("It is a prime number")

x=int(input("Enter the number : "))
prime_number(x)