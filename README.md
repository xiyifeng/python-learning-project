# Python 学习项目

一个综合性项目，用于演示基本的 Python 概念，包括变量、控制流、函数和面向对象编程。

## 项目结构

```
python-learning-project/
├── main.py             # 程序入口文件
├── __init__.py         # 包初始化文件
├── modules/            # 按不同 Python 概念组织的模块
│   ├── variables.py    # 变量模块
│   ├── control_flow.py # 控制流模块
│   ├── functions.py    # 函数模块
│   ├── classes.py      # 类模块
│   └── sorting.py      # 排序算法模块
└── tests/              # 所有功能的单元测试
    ├── test_variables.py
    ├── test_control_flow.py
    ├── test_functions.py
    ├── test_classes.py
    └── test_sorting.py
```

## 安装步骤

1. 克隆或下载项目目录
2. 确保系统已安装 Python 3.x
3. (可选) 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 系统使用: venv\Scripts\activate
   ```

## 使用方法

运行主程序：
```bash
cd python-learning-project
python main.py
```

## 执行测试

运行全部单元测试：
```bash
cd python-learning-project
python -m unittest discover
```

运行特定测试：
```bash
python -m unittest tests.test_variables
python -m unittest tests.test_control_flow
python -m unittest tests.test_functions
python -m unittest tests.test_classes
python -m unittest tests.test_sorting
```

## 模块说明

### 1. 变量模块 (`modules/variables.py`)
演示 Python 变量和数据类型：
- 整数、浮点数、字符串和布尔值
- 列表、字典、元组和集合

### 2. 控制流模块 (`modules/control_flow.py`)
演示 Python 控制流语句：
- If/elif/else 语句
- For 和 while 循环
- Try/except 异常处理

### 3. 函数模块 (`modules/functions.py`)
演示 Python 函数定义和使用：
- 基本函数创建
- 默认参数
- 可变参数数量
- Lambda 函数

### 4. 类模块 (`modules/classes.py`)
演示 Python 面向对象编程概念：
- 类定义和实例化
- 继承
- 方法重写

### 5. 排序模块 (`modules/sorting.py`)
演示经典排序算法：
- 冒泡排序实现
