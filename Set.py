##SET METHODS
#Example
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
fruits.discard("grape")
fruits.pop()
fruits.update(["mango", "pineapple"])
print("Set after using methods:", fruits)


##SET OPERATIONS
#EXAMPLE PROGRAM
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union_set = A | B
intersection_set = A & B
difference_set = A - B
symmetric_difference_set = A ^ B
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)

##CONVERT SET TO TUPLE,LIST,DICTIONARY
##EXAMPLE PROGRAMS
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print("Set to List:", my_list)
my_tuple = tuple(my_set)
print("Set to Tuple:", my_tuple)
my_dict = {key: "Value" for key in my_set}
print("Set to Dictionary:", my_dict)
