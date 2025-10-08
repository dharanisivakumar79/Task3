# List
list1=[1,3,4,6,8,9,6,5]
print("List : ",list1)
list1.append(10)
print("After append: ",list1)
list1.insert(3,100)
print("After insert: ",list1)
print("Index of value 6: ",list1.index(6))
print("Count of value 6: ",list1.count(6))
list1.reverse()
print("Reverse of the list: ",list1)
list1.remove(8)
print("After remove the value 8: ",list1)
list1.sort()
print("Sort list: ",list1)

# Tuple
Tup1=('apple','orange','grapes','apple')
print("Count: ",Tup1.count('apple'))
print("Index: ",Tup1.index('apple'))

# Set
set1={1,2,3,6,7,4,13}
set2={9,7,8,10,11}
print("Set1=",set1)
print("Set2=",set2)
set1.add(12)
print("After adding: ",set1)
set1.discard(3)
print("After discard: ",set1)
print("Length of the set1=",len(set1))
print("Union of two sets: ",set1|set2)
print("Intersection of two sets: ",set1&set2)
print("Difference of two sets: ",set1-set2)
print("Symmetric difference: ",set1^set2)

# Dictionary
dict={'Rollno':'101','Name':'Abar','Dept':'MCA'}
dict2={'Grade':'A'}
print("Dictionary: ",dict)
print("Items: ",dict.items())
print("Keys: ",dict.keys())
print("Getting values using keys: ",dict.get('Name'))
dict.update(dict2)
print("After Update: ",dict)
dict.pop('Dept')
print("After Popped: ",dict)