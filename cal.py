print("mini calculator")
num1= float(input("enter first number:"))
num2= float(input("enter second number:"))
print("1.addition\n2.subtraction\n3.multiplication\n4.division")
choice=int(input("enter your  choice from 1 to 4:"))
if choice==1:
    print("The addition of two number", num1+num2)
elif choice==2:
    print("The  subtraction of two number", num1-num2)
elif choice==3:
    print("the multipilcation of two number", num1*num2)
elif choice==4:
    print("The division of two numbers", num1/num2)
else:
    print("invalid input")

