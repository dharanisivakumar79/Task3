# Task1
user="Dharani"
password="Dharu"
email="dharu@gmail.com"
n1=input("Enter the username: ")
n2=input("Enter the password: ")
n3=input("Enter the email: ")
if n1==user and n2==password and n3==email:
    print("Login successful")
else:
    print("Incorrect to login")
    

# Task2
n=int(input("Enter the number: "))
if n<=9:
    print("It is single digit number")
elif n<=99:
    print("It is double digit number")
elif n<=100:
    print("It is 3 digit number")
elif n<=1000:
    print("It is 4 digit number")
elif n<=10000:
    print("It is 5 digit number")
else:
    print("Nothing to print")
    

# Task3

n1=int(input("Enter the mark1: "))
n2=int(input("Enter the mark2: "))
n3=int(input("Enter the mark3: "))
n4=int(input("Enter the mark4: "))
n5=int(input("Enter the mark5: "))
total=n1+n2+n3+n4+n5
per=total/5
print(total)
print(per)
if per<25:
    print("F Grade")
elif per>25 and per<45:
    print("E Grade")
elif per>45 and per<50:
    print("D Grade")
elif per>50 and per<60:
    print("C Grade")
elif per>60 and per<80:
    print("B Grade")
elif per>80:
    print("A Grade")
else:
    print("Fail")
    

# Task4

classheld=int(input("Enter the number of classes held: "))
classattend=int(input("Enter the number of classes attended: "))
print(classheld)
print(classattend)
per=classattend/classheld*100
print(per)
if per>=75:
    print("He/She is allowed to write exam")
else:
    print("He/She is not allowed to write exam")
    



