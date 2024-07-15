def add(a, b):
    """
    This function takes two numbers and returns their sum.
    """
    return a + b

def subtract(a, b):
    """
    This function takes two numbers and returns their difference.
    """
    return a - b

def multiply(a, b):
    """
    This function takes two numbers and returns their product.
    """
    return a * b

def divide(a, b):
    """
    This function takes two numbers and returns their division result.
    If the divisor is zero, it returns 'None'.
    """
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b