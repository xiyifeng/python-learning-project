"""
Control Flow Module

Demonstrates Python control flow statements
"""

def demonstrate_control_flow():
    """Demonstrate if statements, loops, and error handling."""
    print("=== Control Flow ===")
    
    # If statements
    temperature = 25
    print(f"Temperature: {temperature}")
    if temperature > 30:
        print("It's hot outside!")
    elif temperature > 20:
        print("It's warm outside!")
    else:
        print("It's cool outside!")
    
    # For loop
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(f"Number {i}")
    
    # While loop
    print("\nCounting down from 5 to 1:")
    count = 5
    while count > 0:
        print(f"Count: {count}")
        count -= 1
    
    # Error handling
    print("\nDemonstrating error handling:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Execution completed.")
