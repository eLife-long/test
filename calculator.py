def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Example usage
if __name__ == "__main__":
    print("Addition:", add(2, 3))
    print("Subtraction:", subtract(5, 2))
    print("Multiplication:", multiply(3, 4))
    print("Division:", divide(10, 2))