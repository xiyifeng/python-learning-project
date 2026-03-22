"""
Variables Module

Demonstrates Python variables and data types
"""

def demonstrate_variables():
    """Demonstrate variable declaration and basic data types."""
    print("=== Variables and Data Types ===")
    
    # 整数类型，表示年龄
    age = 25
    print(f"Integer: age = {age} ({type(age)})")  # 输出整数类型信息
    
    # 浮点数类型，表示价格
    price = 9.99
    print(f"Float: price = {price} ({type(price)})")  # 输出浮点数类型信息
    
    # 字符串类型，表示姓名
    name = "Alice"
    print(f"String: name = '{name}' ({type(name)})")  # 输出字符串类型信息
    
    # 布尔类型，表示学生身份
    is_student = True
    print(f"Boolean: is_student = {is_student} ({type(is_student)})")  # 输出布尔类型信息
    
    # 列表类型，存储字符串元素
    fruits = ["apple", "banana", "cherry"]
    print(f"List: fruits = {fruits} ({type(fruits)})")  # 输出列表类型信息
    
    # 字典类型，存储键值对数据
    person = {"name": "Bob", "age": 30}
    print(f"Dictionary: person = {person} ({type(person)})")  # 输出字典类型信息
    
    # 元组类型，存储不可变数据
    coordinates = (10, 20)
    print(f"Tuple: coordinates = {coordinates} ({type(coordinates)})")  # 输出元组类型信息
    
    # 集合类型，自动去重存储
    unique_numbers = {1, 2, 3, 2, 1}
    print(f"Set: unique_numbers = {unique_numbers} ({type(unique_numbers)})")  # 输出集合类型信息
