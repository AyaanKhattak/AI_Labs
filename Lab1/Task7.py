def simple_calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"
    
print("Result of calculation:", simple_calculator(10, 5, '+'))