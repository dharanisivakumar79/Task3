
#Tasl1

a=int(input("Enter the num1: "))
b=int(input("Enter the num2: "))
sym=input("Enter only the symbol not in words: ")
if sym=="+":
    c=a+b
    print("The addition is ",c)
elif sym=="-":
    c=a-b
    print("The sub is ",c)
elif sym=="*":
    c=a*b
    print("The multiple is ",c)
elif sym=="/":
    c=a/b
    print("The division is ",c)
elif sym=="%":
    c=a%b
    print("The modulus is ",c)
elif sym=="**":
    c=a**b
    print("The expotential is ",c)
else:
    print("Only symbols")


#Task2

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

def calculator():
    num1=int(input("Enter the num1: "))
    num2=int(input("Enter the num2: "))
    sym=input("Enter only the symbol not in words: ")
    if sym=="+":
        add(num1,num2)
    elif sym=="-":
        sub(num1,num2)
    elif sym=="*":
        mul(num1,num2)
    elif sym=="/":
        div(num1,num2)
calculator()

