def check_prime_number(n):
    for i in range (2,n-1):
        temp=n
        if(temp%i==0):
            temp%=i

    if(temp==n):
        print("\nIt is prime number")
    else:
        print("\nIt is not a prime number")



x=int(input("Enter the number"))
check_prime_number(x)