def leap_year_evaluate(x):
    if(x%4==0):
        print("It is leap year")

    else:
        print("It is not leap year")

n=int(input("Enter the year :"))
leap_year_evaluate(n)