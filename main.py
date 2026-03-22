"""
Python Learning Project - Main Entry Point

This script demonstrates basic Python concepts including:
- Variables and data types
- Control flow
- Function definitions
- Class implementation
"""

# Import local modules
from modules.variables import demonstrate_variables
from modules.control_flow import demonstrate_control_flow
from modules.functions import demonstrate_functions
from modules.classes import demonstrate_classes

def main():
    """Main function to run all demonstrations."""
    print("=== Python Learning Project ===\n")
    
    # Demonstrate core concepts
    demonstrate_variables()
    demonstrate_control_flow()
    demonstrate_functions()
    demonstrate_classes()
    
    print("\n=== Demonstration Complete ===")

if __name__ == "__main__":
    main()
