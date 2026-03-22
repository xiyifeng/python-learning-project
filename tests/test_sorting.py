"""
Test cases for sorting module
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.sorting import bubble_sort

class TestSorting(unittest.TestCase):
    """Test class for sorting algorithms"""
    
    def test_bubble_sort_basic(self):
        """Test basic bubble sort functionality"""
        # 测试基本排序功能
        unsorted = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_empty_list(self):
        """Test bubble sort with empty list"""
        # 测试空列表
        unsorted = []
        expected = []
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_single_element(self):
        """Test bubble sort with single element"""
        # 测试单个元素
        unsorted = [42]
        expected = [42]
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_already_sorted(self):
        """Test bubble sort with already sorted list"""
        # 测试已排序列表
        unsorted = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_reverse_sorted(self):
        """Test bubble sort with reverse sorted list"""
        # 测试逆序列表
        unsorted = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_duplicates(self):
        """Test bubble sort with duplicate elements"""
        # 测试重复元素
        unsorted = [3, 7, 3, 1, 7, 1]
        expected = [1, 1, 3, 3, 7, 7]
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_negative_numbers(self):
        """Test bubble sort with negative numbers"""
        # 测试负数
        unsorted = [-1, -5, 3, 0, -3, 2]
        expected = [-5, -3, -1, 0, 2, 3]
        result = bubble_sort(unsorted)
        self.assertEqual(result, expected)
    
    def test_bubble_sort_original_unchanged(self):
        """Test that original array is not modified"""
        # 测试原始数组未被修改
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        bubble_sort(original)
        self.assertEqual(original, original_copy)

if __name__ == '__main__':
    unittest.main()
