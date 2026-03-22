"""
Sorting Module

Contains implementations of various sorting algorithms
"""

def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    Args:
        arr (list): 待排序的数组
        
    Returns:
        list: 排序后的数组
        
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    # 创建数组副本以避免修改原数组
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换
        swapped = False
        
        # 内层循环进行相邻元素比较
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序
        if not swapped:
            break
            
    return sorted_arr
