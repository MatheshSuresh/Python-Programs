x=int(input("Enter your number :"))
y=int(input("Enter your number :"))
z=int(input("Enter your number :"))
if(x>y)and(x>z):
    print("x is greatest")
elif(y>z)and(y>x):
    print("y is greater")
else:
    print("z is greater")
