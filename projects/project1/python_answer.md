## 1. What is a class object in Python?
In Python, a **class** objext is something you use that you will have to submit inside a python. For the python to read.

```python
class Comb:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        my_comb = Comb("Hair", 3)  # 'my_comb' is a class object

## 2. What is a docstring?
These are quotes that you use inside sum of two numbers.

def add(e, f):
    """
    These are quotes that you can use inside of two numbers.
    """
    return e + f

## 3. How to define __init__ in a class? 
This used inside of a python __init__ is automatically called inside Python whenever you create a new object.

class Comd:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_comb = Comb("Hair", 3)  # __init__ is called here to initialize 'my_comb'

## 4. How do you let functions fail gracefully?
If the function fail that means it is not insert in the program correclty. Than you will receive errors.

def divide(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Error: Both arguments must be numbers."
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

## 5.  What's a standard practice of a return statement?
This means that the statement is coming back to you.

def add(e, f):
    return e + f


