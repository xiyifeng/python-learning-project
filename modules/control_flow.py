"""
Control Flow Module

Demonstrates Python control flow statements
"""

def demonstrate_control_flow():
    """Demonstrate if statements, loops, and error handling."""
    print("=== Control Flow ===")
    
    # If语句示例
    temperature = 25
    print(f"温度值: {temperature}")
    # 条件判断示例
    if temperature > 30:
        print("天气很热！")
    elif temperature > 20:
        print("天气温暖！")
    else:
        print("天气凉爽！")
    
    # For循环示例
    print("\n从1计数到5:")
    for i in range(1, 6):
        # 打印当前数字
        print(f"数字 {i}")
    
    # While循环示例
    print("\n从5倒数到1:")
    count = 5
    while count > 0:
        # 打印当前倒数
        print(f"倒数: {count}")
        count -= 1
    
    # 错误处理示例
    print("\n演示错误处理:")
    try:
        # 故意引发除零错误
        result = 10 / 0
    except ZeroDivisionError:
        # 捕获除零错误
        print("不能除以零！")
    finally:
        # 最终执行的代码
        print("执行完成。")
