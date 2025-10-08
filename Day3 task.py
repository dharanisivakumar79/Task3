# task 1
n=int(input("Enter the number: "))
if(n%2==0):
    print("It is even number")
else:
    print("It is odd number")
    
# task 2
age=int(input("Enter the age: "))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# task 3
num=int(input("Enter the number: "))
if(num%3==0 and num%5==0):
    print("Fizz Buzz")
elif(num%5==0):
    print("Buzz")
elif (num%3==0):
    print("Fizz")
else:
    print("Give number that only divisible by 3 and 5")
