# Basic Calculator Program

def calculator():
    """
    This function prompts the user to input a number, an operator (+, -, *, /), 
    and another number, then performs the corresponding mathematical operation 
    and displays the result. It also handles invalid inputs and division by zero errors.
    """
    try:
        # Get user input for the first number
        num1 = float(input("Enter first number: "))
        
        # Get user input for the mathematical operator
        operator = input("Enter operation (+, -, *, /): ")
        
        # Validate the operator
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please use +, -, *, or /.")
            return
        
        # Get user input for the second number
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on the chosen operator
        if operator == '+':
            result = num1 + num2  # Addition
        elif operator == '-':
            result = num1 - num2  # Subtraction
        elif operator == '*':
            result = num1 * num2  # Multiplication
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2  # Division
        
        # Print the result
        print(f"Result: {num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the calculator function
if __name__ == "__main__":
    calculator()