# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to drive the calculator
def calculator():
    print("Simple Arithmetic Calculator")
    
    # Input: two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Input: operation choice
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("\nEnter your choice (1/2/3/4): ")

    # Perform the chosen operation
    if choice == '1':
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
