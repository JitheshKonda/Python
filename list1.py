#Creation of Empty list
kiran=[]
print(type(kiran))
print(kiran)
print()

#creation of list with various types of data
kiran=[1,2.2,"listExample"]
print(kiran)
print(type(kiran))
print()

#Accessing list by using positive and negative index number 
Fruits=['mango','apple','banana']
print(Fruits[1])
print(Fruits[-1])
print()

#Slicing of lists 
Animals=["Dog","Cat","Cow","Lion","Tiger"]
print(Animals[0:4:2])
print(Animals[0:2])
print(Animals[:2])
print(Animals[0:])
print(Animals[4:0:-2])
print(Animals[-4:2])
print(Animals[-3:4:1])
print(Animals[0:3+1])
print(Animals[0:4:-2])
print(Animals[-1])
print(Animals[-1:4:-2])
print(Animals[4:-2])
print(Animals[4:0])
print(Animals[::])
print(Animals[:])
print(Animals[::-1])
print(Animals[2:1])
print(Animals[4:-2])
print()


#Adding of two lists
list_1=[1,2,3]
list_2=[4,5,6]
print(list_1 + list_2)
print()

#multiply list
a=[5,2.2]
print(a*3)
print()

#Check given element present in list or not
a=["Pooji","vinay",1,2.3]
print (1 in a)
print(5 in a)
print()

#built in functions in list
num=[10,20,30,40]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print()

#any() and all() returns either true or false but list contain 0's all() shows false,any() always returns true only
print(any([1,2,0,0,3,0]))
print(all([1,2,3,4,5]))
print()

#list methods
students=['Ram','Ravi','Vinay','Sweety','Sunny']
print(students.count("Ravi"))
print(students.index("Sunny"))
students.insert(5,"Arjun")
print(students)
students.reverse()
print(students)
print(len(students))
students.sort()
print(students)

students.sort(reverse=True)
print(students)
a=students
print(id(students))
print(id(a))
print(a==students)

b= students.copy()
print(b)
students.insert(0,"bunny")
print(students)
students.remove("Ravi")
print(students)
print(students.pop(0))
students.clear()
print(students)
print()

#Travarsing of lists
age=[12,14,18,24]
for index in range(len(age)):
    print(f"indexValue of'{age[index]}'is {index}")
print()

#Nested lists-->A list inside another list
asia=[['India','paris','Kashmir'],['Korea','UK','US'],['bihar','china','japan']]
print(asia)
asia[0][1]="Patna"
print(asia[0][1])
print(asia[0])
print(asia[2][1])

print()

#print list elements through user
list_items=[]
total_items=int(input("Enter the number of elements:"))
for i in range(total_items):
    item=input("Enter the list item:")
    list_items.append(item)
    print(f"List items are {list_items}")
print()

#Delete list element in list by using remove(),pop(),delete(),clear()
#del()-->used to delete a value through index and slice
a=[1,2,3,6,7,9,5]
del a[2:4]
print(a)
del a[3]
print(a)
print()

#pop()-->used to pop a value by using index value
a=[1,2,3,6,7,9,5]
a.pop(3)
print(a)
print()

#remove() used to remove a value from list 
a=[4,8,24,14,5,2,3,6]
a.remove(14)
print(a)
