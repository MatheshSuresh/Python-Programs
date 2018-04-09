def addition(a,b):
    print(a+b)


def subraction(a,b):
    print(a-b)


def multiplication(a,b):
    print(a*b)


def division(a,b):
    print(a/b)


x=int(input("\nEnter the number"))
y=int(input("\nEnter the number"))

print("1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n")
z=int(input("Enter your choice :"))
if(z==1):
    addition(x,y)


elif(z==2):
    subraction(x,y)


elif(z==3):
    multiplication(x,y)


elif(z==4):
    division(x,y)

else:
    print("Try other")