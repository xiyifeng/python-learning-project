"""
Classes Module

Demonstrates Python object-oriented programming concepts
"""

def demonstrate_classes():
    """Demonstrate class definition, inheritance, and method usage."""
    print("=== Classes ===")
    
    # Basic class definition
    class Dog:
        """
        一个简单的狗类
        
        属性:
            name (str): 狗的名字
            age (int): 狗的年龄（岁）
            
        方法:
            bark: 让狗叫
        """
        def __init__(self, name, age):
            """
            初始化新的狗实例
            
            参数:
                name (str): 狗的名字
                age (int): 狗的年龄（岁）
            """
            self.name = name
            self.age = age
            
        def bark(self):
            """
            让狗叫
            
            返回:
                str: 表示狗叫声的字符串
            """
            return f"{self.name} says Woof!"
    
    # Create instance and demonstrate methods
    my_dog = Dog("Buddy", 3)
    print(f"Basic class: {my_dog.bark()}")
    print(f"Attributes: {my_dog.name} is {my_dog.age} years old")
    
    # Inheritance
    class GoldenRetriever(Dog):
        """
        金毛寻回犬类，继承自Dog类
        
        继承Dog类的所有功能，并添加了
        金毛特有的方法
        """
        def fetch(self):
            """
            金毛特有的取物方法
            
            返回:
                str: 表示金毛取物动作的字符串
            """
            return f"{self.name} fetched the ball!"
    
    # Create subclass instance
    my_golden = GoldenRetriever("Max", 2)
    print(f"\nInheritance: {my_golden.bark()}")
    print(f"Specialized method: {my_golden.fetch()}")
    
    # Method overriding
    class LoudDog(Dog):
        """
        大声狗类，继承自Dog类
        
        重写了bark方法以产生更大的声音
        """
        def bark(self):
            """
            重写父类的bark方法
            
            返回:
                str: 表示大声狗叫声的字符串
            """
            return f"{self.name} shouts WOOF!"
    
    # Create overridden class instance
    my_loud_dog = LoudDog("Rex", 5)
    print(f"\nMethod overriding: {my_loud_dog.bark()}")
