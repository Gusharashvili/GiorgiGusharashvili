class Calculator:
    def __init__(self, num1, num2):
        # Initialize the calculator with two numbers
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # Add two numbers
        return self.num1 + self.num2

    def subtract(self):
        # Subtract num2 from num1
        return self.num1 - self.num2

    def multiply(self):
        # Multiply two numbers
        return self.num1 * self.num2

    def divide(self):
        # Check for division by zero and perform division if possible
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Cannot divide by zero"

    def perform_operation(self, operation):
        # Perform the specified operation based on user input
        if operation == 'add':
            return self.add()
        elif operation == 'subtract':
            return self.subtract()
        elif operation == 'multiply':
            return self.multiply()
        elif operation == 'divide':
            return self.divide()
        else:
            return "Error: Invalid operation"


# Main code
while True:
    answer = input("Do you want to quit? (Type 'quit' to exit): ")
    if answer.lower() == "quit":
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    # Create an instance of the Calculator class
    calculator_instance = Calculator(num1, num2)
    
    # Perform the specified operation and get the result
    result = calculator_instance.perform_operation(operation)
    
    # Display the result
    print(f"Result: {result}")

    # Writing result to file
    with open("calculator_results.txt", "a") as file:
        file.write(f"{num1} {operation} {num2} = {result}\n")

