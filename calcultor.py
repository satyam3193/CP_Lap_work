#code for calculator using if else

a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Division")
chose =int(input("Enter your choice:12"))
if chose==1:
    print(a+b)
elif chose==2:
        print(a-b)
elif chose==3:
        print(a*b)
elif chose==4:
        print(a/b)
else:
    print('Enter valid number?')                        