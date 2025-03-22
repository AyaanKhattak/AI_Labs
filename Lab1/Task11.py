def calculator(a, b, operation='+', output_format='float'):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both operands must be numbers.")
    if operation not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operation. Choose from '+', '-', '*', '/'")
    
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
    
    if output_format == 'integer':
        return round(result)
    elif output_format == 'float':
        return float(result)
    else:
        raise ValueError("Invalid output format. Choose 'integer' or 'float'.")

print("Calculator Result:", calculator(10, 3, '/', 'integer'))