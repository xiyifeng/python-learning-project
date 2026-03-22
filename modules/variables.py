"""
Variables Module

Demonstrates Python variables and data types
"""

def demonstrate_variables():
    """Demonstrate variable declaration and basic data types."""
    print("=== Variables and Data Types ===")
    
    # Integer
    age = 25
    print(f"Integer: age = {age} ({type(age)})")
    
    # Float
    price = 9.99
    print(f"Float: price = {price} ({type(price)})")
    
    # String
    name = "Alice"
    print(f"String: name = '{name}' ({type(name)})")
    
    # Boolean
    is_student = True
    print(f"Boolean: is_student = {is_student} ({type(is_student)})")
    
    # List
    fruits = ["apple", "banana", "cherry"]
    print(f"List: fruits = {fruits} ({type(fruits)})")
    
    # Dictionary
    person = {"name": "Bob", "age": 30}
    print(f"Dictionary: person = {person} ({type(person)})")
    
    # Tuple
    coordinates = (10, 20)
    print(f"Tuple: coordinates = {coordinates} ({type(coordinates)})")
    
    # Set
    unique_numbers = {1, 2, 3, 2, 1}
    print(f"Set: unique_numbers = {unique_numbers} ({type(unique_numbers)})")
