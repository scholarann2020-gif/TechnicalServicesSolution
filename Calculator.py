import math

print('''     
     🌟 Welcome to Cal-AI 🌟
   Your favourite one to calculate
  Difficult questions you cannot solve...
But at the end I say — nothing is impossible!
                           ''')

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def mod(a, b):
    if b == 0:
        return "Error: Modulus by zero!"
    return a % b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Cannot find square root of negative number!"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial not defined for negative numbers!"
    return math.factorial(a)

def average(numbers):
    return sum(numbers) / len(numbers)

def even_odd(a):
    return "Even" if a % 2 == 0 else "Odd"

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Main Program Loop
while True:
    print('''
    ===============================
           🧮 Cal-AI Menu 🧠
    ===============================
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Power
    7. Square Root
    8. Factorial
    9. Average of numbers
    10. Even/Odd Check
    11. GCD
    12. LCM
    13. Exit
    ''')

    choice = input("Enter your choice (1-13): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", sub(a, b))

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", mul(a, b))

    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", div(a, b))

    elif choice == '5':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", mod(a, b))

    elif choice == '6':
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result:", power(a, b))

    elif choice == '7':
        a = float(input("Enter number: "))
        print("Result:", sqrt(a))

    elif choice == '8':
        a = int(input("Enter a number: "))
        print("Result:", factorial(a))

    elif choice == '9':
        nums = list(map(float, input("Enter numbers separated by space: ").split()))
        print("Result:", average(nums))

    elif choice == '10':
        a = int(input("Enter a number: "))
        print("Result:", even_odd(a))

    elif choice == '11':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", gcd(a, b))

    elif choice == '12':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", lcm(a, b))

    elif choice == '13':
        print("Thank you for using Cal-AI! 👋")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 13.")

    print("\n---------------------------------\n")
