"""
Test cases for functions module
"""
import unittest
from modules.functions import demonstrate_functions
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestFunctions(unittest.TestCase):
    """Test function definitions and usage"""
    def test_function_demonstration(self):
        """Test functions execution without errors"""
        try:
            demonstrate_functions()
            self.assertTrue(True)  # If no errors, test passes
        except Exception as e:
            self.fail(f"Functions demonstration failed with error: {str(e)})")

if __name__ == '__main__':
    unittest.main()
