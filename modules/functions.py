"""
Functions Module

Demonstrates Python function definitions and usage
"""

def demonstrate_functions():
    """Demonstrate function definition, parameters, and return values."""
    print("=== Functions ===")
    
    # 基本函数示例
    def greet(name):
        """
        返回问候语
        
        参数:
            name (str): 需要问候的人名
        返回:
            str: 包含人名的问候语
        """
        return f"Hello, {name}!"
    
    message = greet("Alice")
    print(f"Basic function: {message}")
    
    # 带有默认参数的函数
    def power(base, exponent=2):
        """
        计算指数幂运算（默认平方）
        
        参数:
            base (int): 基数
            exponent (int, optional): 指数，默认值为2
        返回:
            int: 计算结果
        """
        return base ** exponent
    
    print(f"Default parameter: 5^2 = {power(5)}")
    print(f"Custom parameter: 2^4 = {power(2, 4)}")
    
    # 可变参数函数
    def sum_all(*numbers):
        """
        计算任意数量数字的总和
        
        参数:
            *numbers (int): 可变数量的数字参数
        返回:
            int: 所有数字的总和
        """
        return sum(numbers)
    
    print(f"Variable arguments: {sum_all(1, 2, 3, 4, 5)}")
    
    # Lambda函数示例
    square = lambda x: x * x
    print(f"Lambda函数: {square(5)}")
