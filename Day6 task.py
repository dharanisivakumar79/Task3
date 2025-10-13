# Task1
n=0
while (True):
	n+=1
	print (n, "Dharani")
	if n>=10:
		break

#Task2
list1=[]
list2=[]
n=0
while n<=100:
	if n%2==0:
		list1.append(n)
	else:
		list2.append(n)
	n+=1
print("Even numbers: ",list1)
print("Odd Numbers: ", list2)