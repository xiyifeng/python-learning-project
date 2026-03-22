"""
Classes Module

Demonstrates Python object-oriented programming concepts
"""

def demonstrate_classes():
    """Demonstrate class definition, inheritance, and method usage."""
    print("=== Classes ===")
    
    # Basic class definition
    class Dog:
        """A simple Dog class."""
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
        def bark(self):
            """Make the dog bark."""
            return f"{self.name} says Woof!"
    
    # Create instance and demonstrate methods
    my_dog = Dog("Buddy", 3)
    print(f"Basic class: {my_dog.bark()}")
    print(f"Attributes: {my_dog.name} is {my_dog.age} years old")
    
    # Inheritance
    class GoldenRetriever(Dog):
        """A GoldenRetriever subclass of Dog."""
        def fetch(self):
            """Specialized method for Golden Retrievers."""
            return f"{self.name} fetched the ball!"
    
    # Create subclass instance
    my_golden = GoldenRetriever("Max", 2)
    print(f"\nInheritance: {my_golden.bark()}")
    print(f"Specialized method: {my_golden.fetch()}")
    
    # Method overriding
    class LoudDog(Dog):
        """A Dog subclass with louder bark."""
        def bark(self):
            """Override parent's bark method."""
            return f"{self.name} shouts WOOF!"
    
    # Create overridden class instance
    my_loud_dog = LoudDog("Rex", 5)
    print(f"\nMethod overriding: {my_loud_dog.bark()}")
