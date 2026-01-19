#map() – Square of All Numbers
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)

#convert celsius to fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

#Using filter function print evem numbers
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#Using filter function to print prime numbers 
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
primes = list(filter(
    lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)),
  numbers
))
print(primes)

##USing reduce to print sum of elements
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)

#USing reduce to print product of elements
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(product)

#Function with return+map
def cube(x):
    return x ** 3
numbers = [1, 2, 3, 4]
cubes = list(map(cube, numbers))
print(cubes)


