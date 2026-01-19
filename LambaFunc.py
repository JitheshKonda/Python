#Example programs for lamba function
#Add two numbers
add = lambda a, b: a + b
print(add(10, 20))

#Square of a number
square = lambda x: x * x
print(square(5))

#cube of a number
cube = lambda x: x * x * x
print(cube(8))

#Even or Odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))

#Check natural number
is_natural = lambda x: x > 0 and isinstance(x, int)
print(is_natural(5))
print(is_natural(-3))
print(is_natural(0))

#Check Given number is prime or not
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print(is_prime(7))
print(is_prime(10))

#Using lamba Print a multiplication table 
table = lambda n: [print(f"{n} x {i} = {n*i}") for i in range(1, 11)]
table(n)


