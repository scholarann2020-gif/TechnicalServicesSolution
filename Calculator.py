print('''     
     Welcome to the Cal-AI
   your favourite one to calculate
  Difficult Question u cannot solve
But At the end I say nothing is impossible
                           ''')

print("Enter 2 Numbers")
a = int(input("First number: "))
b = int(input("Second number: "))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def mod(a, b):
    if b == 0:
        return "Error: Modulo by zero"
    return a % b

def power(a, b):
    return a ** b

print("\n--- Results ---")
print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))
print("Modulus:", mod(a, b))
print("Power:", power(a, b))
