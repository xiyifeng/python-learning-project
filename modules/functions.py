"""
Functions Module

Demonstrates Python function definitions and usage
"""

def demonstrate_functions():
    """Demonstrate function definition, parameters, and return values."""
    print("=== Functions ===")
    
    # Basic function
    def greet(name):
        """Return a greeting message."""
        return f"Hello, {name}!"
    
    message = greet("Alice")
    print(f"Basic function: {message}")
    
    # Function with default parameters
    def power(base, exponent=2):
        """Calculate power with default exponent."""
        return base ** exponent
    
    print(f"Default parameter: 5^2 = {power(5)}")
    print(f"Custom parameter: 2^4 = {power(2, 4)}")
    
    # Variable number of arguments
    def sum_all(*numbers):
        """Sum all provided numbers."""
        return sum(numbers)
    
    print(f"Variable arguments: {sum_all(1, 2, 3, 4, 5)}")
    
    # Lambda function
    square = lambda x: x * x
    print(f"Lambda function: {square(5)}")
