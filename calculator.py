def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Division by zero is not allowed"
    return a/b
print("simple calculator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
choice=input("enter choice: ")
a=float(input("enter first number"))
b=float(input("enter second number"))
if choice=='1':
    print("result1: ",add(a,b))
elif choice=='2':
    print("result1: ",subtract(a,b))
elif choice=='3':
    print("result1: ",multiply(a,b))
elif choice=='4':
    print("result1: ",divide(a,b))
else:
    print("invalid input")