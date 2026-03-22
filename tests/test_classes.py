"""
Test cases for classes module
"""
import unittest
from modules.classes import demonstrate_classes
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestClasses(unittest.TestCase):
    """Test class definitions and inheritance"""
    def test_class_demonstration(self):
        """Test classes execution without errors"""
        try:
            demonstrate_classes()
            self.assertTrue(True)  # If no errors, test passes
        except Exception as e:
            self.fail(f"Classes demonstration failed with error: {str(e)})")

if __name__ == '__main__':
    unittest.main()
