##TUPLE METHODS
# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple", "banana")

# 1. count() - returns how many times an element appears
apple_count = fruits.count("apple")
print("Apple appears:", apple_count, "times")

# 2. index() - returns the index of the first occurrence of an element
banana_index = fruits.index("banana")
print("First banana is at index:", banana_index)

##TUPLE OPERATIONS

# Creating tuples
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

# 1. Concatenation
concat = tuple1 + tuple2
print("Concatenation:", concat)

# 2. Repetition
repeat = tuple1 * 2
print("Repetition:", repeat)

# 3. Membership test
print("Is 3 in tuple1?", 3 in tuple1)
print("Is 7 not in tuple1?", 7 not in tuple1)

# 4. Length of tuple
print("Length of tuple1:", len(tuple1))

# 5. Max and Min
print("Max of tuple2:", max(tuple2))
print("Min of tuple2:", min(tuple2))

# 6. Iteration
print("Elements of tuple1:")
for item in tuple1:
    print(item, end=" ")
print()

# 7. Slicing
print("tuple2[1:3]:", tuple2[1:3])
