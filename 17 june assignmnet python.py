#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### 1. What is the role of try and except blocks?
"""The `try` and `except` blocks in Python are used for exception handling. The code within the `try` block is executed first, and if an exception occurs, the control is transferred to the `except` block. This allows the program to handle errors gracefully without crashing.
"""
### 2. What is the syntax for a basic try-except block?

try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception


### 3. What happens if an exception occurs inside a try block and there is no matching except block?
""If an exception occurs inside a `try` block and there is no matching `except` block to handle it, the program will terminate, and Python will display a traceback, showing the error message and the point in the code where the exception occurred.
""


# In[ ]:



### 4. What is the difference between using a bare except block and specifying a specific exception type?
"""Bare `except` block: Catches all exceptions, which can make debugging difficult as it may also catch unexpected exceptions that were not intended to be caught.
Specific exception type: Catches only the specified exception, making the code more predictable and easier to debug.
"""
try:
    risky_operation()
except:  # Bare except block
    print("An error occurred")
    
    
try:
    risky_operation()
except ValueError:  # Specific exception type
    print("A ValueError occurred")


# In[ ]:


### 5. Can you have nested try-except blocks in Python? If yes, then give an example.
"""Yes, you can have nested `try-except` blocks in Python.
"""
try:
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
    except ZeroDivisionError:
        print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")


# In[ ]:


### 6. Can we use multiple except blocks? If yes, then give an example.
Yes, you can use multiple `except` blocks to handle different types of exceptions.

**Example:**
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```


# In[ ]:


### 7. Write the reason due to which the following errors are raised:

"""a. EOFError: Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data.
b. FloatingPointError: Raised when a floating-point operation fails (rarely used as most floating-point errors do not raise this exception).
c. IndexError: Raised when trying to access an index that is out of range for a list or a sequence.
d. MemoryError: Raised when an operation runs out of memory but can still be caught and handled.
e. OverflowError: Raised when the result of an arithmetic operation is too large to be represented by the destination type.
f. TabError: Raised when the indentation of code contains inconsistent use of tabs and spaces.
g. ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
"""


# In[ ]:


### 8. Write code for the following scenarios and add try-except blocks to it.
"""
a. Program to divide two numbers:"""
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")


# In[ ]:


"""b. Program to convert a string to an integer:
"""
try:
    s = input("Enter a number: ")
    number = int(s)
    print(f"Converted number is: {number}")
except ValueError:
    print("Error: The input is not a valid integer.")


# In[ ]:


"""c. Program to access an element in a list:
"""

try:
    my_list = [10, 20, 30, 40, 50]
    index = int(input("Enter the index of the element you want to access: "))
    print(f"The element at index {index} is {my_list[index]}")
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")


# In[ ]:


"""d. Program to handle a specific exception:
"""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


# In[ ]:


"""e. Program to handle any exception:"""


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"The result is: {result}")
except Exception as e:
    print(f"An error occurred: {e}")


# In[ ]:




