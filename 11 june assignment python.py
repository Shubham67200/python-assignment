#!/usr/bin/env python
# coding: utf-8

# In[4]:


### 1. What is a lambda function in Python, and how does it differ from a regular function?

"""A lambda function in Python is a small, anonymous function defined using the `lambda` keyword. Unlike regular functions, which are defined using the `def` keyword and require a name, lambda functions are typically used for short, simple operations and do not have a name. They can have any number of arguments but only a single expression, which is evaluated and returned.
"""

# Regular function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y


# In[5]:


### 2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use them?
"""
Yes, a lambda function in Python can have multiple arguments. You can define and use them by simply listing the arguments after the `lambda` keyword and separating them with commas.
"""

multiply = lambda x, y: x * y
result = multiply(3, 4)  # Output: 12



# In[20]:


### 3. How are lambda functions typically used in Python? Provide an example use case.

"""Lambda functions are typically used in Python for short, simple operations where defining a full function using `def` would be overkill. They are often used in combination with functions like `map()`, `filter()`, and `sort()`.
"""

# Using lambda with map to square each element in a list
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Output: [1, 4, 9, 16]



# In[21]:


### 4. What are the advantages and limitations of lambda functions compared to regular functions in Python?
"""
Advantages:
Conciseness: Lambda functions allow for the creation of small, anonymous functions in a single line, which can make the code more concise.
Quick and Simple: Ideal for short operations, especially when used as arguments to higher-order functions like `map()`, `filter()`, or `sort()`.

Limitations:
Limited Functionality: Lambda functions are limited to a single expression and cannot contain multiple statements or annotations.
Readability: While concise, lambda functions can make the code less readable, especially for more complex operations.
No Name: Lambda functions do not have a name, making debugging and tracing harder."""


# In[22]:


### 5. Are lambda functions in Python able to access variables defined outside of their own scope? Explain with an example.

"""Yes, lambda functions in Python can access variables defined outside their own scope. This is known as a closure. The lambda function "remembers" the value of the variable from the surrounding scope.
"""
x = 10
add_x = lambda y: x + y  # 'x' is accessed from the outer scope
result = add_x(5)  # Output: 15



# In[23]:


### 6. Write a lambda function to calculate the square of a given number.


square = lambda x: x ** 2
result = square(5)  # Output: 25



# In[24]:


### 7. Create a lambda function to find the maximum value in a list of integers.


max_value = lambda lst: max(lst)
result = max_value([1, 7, 3, 9, 5])  # Output: 9


# In[25]:


### 8. Implement a lambda function to filter out all the even numbers from a list of integers.


filter_even = lambda lst: list(filter(lambda x: x % 2 != 0, lst))
result = filter_even([1, 2, 3, 4, 5, 6])  # Output: [1, 3, 5]


# In[26]:


### 9. Write a lambda function to sort a list of strings in ascending order based on the length of each string.


sort_by_length = lambda lst: sorted(lst, key=lambda s: len(s))
result = sort_by_length(['apple', 'fig', 'banana', 'date'])  # Output: ['fig', 'date', 'apple', 'banana']


# In[27]:


### 10. Create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists.

common_elements = lambda lst1, lst2: list(filter(lambda x: x in lst2, lst1))
result = common_elements([1, 2, 3, 4], [3, 4, 5, 6])  # Output: [3, 4]


# In[28]:


### 11. Write a recursive function to calculate the factorial of a given positive integer.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)  # Output: 120



# In[29]:


### 12. Implement a recursive function to compute the nth Fibonacci number.


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)  # Output: 8



# In[30]:


### 13. Create a recursive function to find the sum of all the elements in a given list.

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

result = sum_list([1, 2, 3, 4, 5])  # Output: 15



# In[19]:


### 14. Write a recursive function to determine whether a given string is a palindrome.


def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

result = is_palindrome("radar")  # Output: True




# In[18]:


### 15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(48, 18)  # Output: 6


# In[ ]:




