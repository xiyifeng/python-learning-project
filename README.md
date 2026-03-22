# Python Learning Project

A comprehensive project designed to demonstrate fundamental Python concepts including variables, control flow, functions, and object-oriented programming.

## Project Structure

```
python-learning-project/
├── main.py             # Entry point demonstrating basic program structure
├── __init__.py         # Package initialization file
├── modules/            # Organized modules for different Python concepts
│   ├── variables.py
│   ├── control_flow.py
│   ├── functions.py
│   └── classes.py
└── tests/              # Unit tests for all functionality
    ├── test_variables.py
    ├── test_control_flow.py
    ├── test_functions.py
    └── test_classes.py
```

## Installation

1. Clone or download the project directory
2. Ensure Python 3.x is installed on your system
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

To run the main demonstration:
```bash
cd python-learning-project
python main.py
```

## Running Tests

To execute all unit tests:
```bash
cd python-learning-project
python -m unittest discover
```

Or run specific tests:
```bash
python -m unittest tests.test_variables
python -m unittest tests.test_control_flow
python -m unittest tests.test_functions
python -m unittest tests.test_classes
```

## Modules Overview

### 1. Variables Module (`modules/variables.py`)
Demonstrates Python variables and data types including:
- Integers, floats, strings, and booleans
- Lists, dictionaries, tuples, and sets

### 2. Control Flow Module (`modules/control_flow.py`)
Demonstrates Python control flow statements:
- If/elif/else statements
- For and while loops
- Error handling with try/except

### 3. Functions Module (`modules/functions.py`)
Demonstrates Python function definitions and usage:
- Basic function creation
- Default parameters
- Variable number of arguments
- Lambda functions

### 4. Classes Module (`modules/classes.py`)
Demonstrates Python object-oriented programming concepts:
- Class definition and instantiation
- Inheritance
- Method overriding
