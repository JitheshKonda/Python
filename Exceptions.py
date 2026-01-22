'''An exception is an error that occurs during the execution of a program.
When an exception occurs:
Python stops the current flow of execution.
'''
#Example 1
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")


#Example 2
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Error: That’s not a valid number!")

#Example 3 (Sum of two numbers)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum is: {a + b}")
except ValueError:
    print("Error: Please enter valid numbers.")

#Example 4 (Simple Calculator)\
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#Example 5
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Result is:", y)
finally:
    print("This always executes.")

#Exammple 6 (Ask a access list element)
numbers = [10, 20, 30, 40]
try:
    index = int(input("Enter index of number: "))
    print(f"Number at index {index} is {numbers[index]}")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Please enter a valid integer.")
finally:
    print("Access attempt finished.")

#Example 7 Reading a file safely
try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found! Please check the filename.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("File content successfully read:\n")
    print(content)
finally:
    print("\nFinished attempting to read the file.")





