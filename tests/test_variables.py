"""
Test cases for variables module
"""
import unittest
from modules.variables import demonstrate_variables

class TestVariables(unittest.TestCase):
    """Test variable and data type demonstrations"""
    def test_variable_demonstration(self):
        """Test variables execution without errors"""
        try:
            demonstrate_variables()
            self.assertTrue(True)  # If no errors, test passes
        except Exception as e:
            self.fail(f"Variables demonstration failed with error: {str(e)})")

if __name__ == '__main__':
    unittest.main()
