# =========================================
# Day 2 – Python Basics (All in One Program)
# Name: Vaishnavi Babanagoud
# =========================================

print("===== PYTHON BASICS PROGRAM =====\n")

# -------------------------------
# 1. Variables & Data Types
# -------------------------------
print("1. Variables & Data Types")

name = "Vaishnavi"
age = 20
marks = 85.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Is Student:", is_student)

print("\nType of variables:")
print(type(name), type(age), type(marks), type(is_student))


# -------------------------------
# 2. Operators
# -------------------------------
print("\n2. Operators")

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Greater than:", a > b)
print("Equal:", a == b)


# -------------------------------
# 3. Loops
# -------------------------------
print("\n3. Loops")

print("For Loop:")
for i in range(1, 6):
    print(i, end=" ")

print("\nWhile Loop:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1


# -------------------------------
# 4. Functions
# -------------------------------
print("\n\n4. Functions")

def greet(name):
    return "Hello " + name

print(greet("Vaishnavi"))


def add_numbers(x, y):
    return x + y

print("Sum using function:", add_numbers(10, 20))


# -------------------------------
# 5. Simple Programs
# -------------------------------
print("\n5. Simple Programs")

# Sum of two numbers
num1 = 10
num2 = 20
print("Sum:", num1 + num2)

# Even or Odd
num = 7
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Factorial
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is:", fact)


print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")
