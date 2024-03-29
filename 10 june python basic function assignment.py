#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1. Difference between built-in function and user-defined function:
   #Built-in function:** These are functions that are pre-defined in Python and are readily available for use without the need for any additional definition. Examples include `print()`, `len()`, `max()`, `min()`, etc.#
   #User-defined function:** These are functions defined by the user according to their specific requirements. They are created using the `def` keyword followed by a function name, parameters, and a block of code defining what the function does. An example could be:
# user defind function
def add(a, b):
    return a + b



# In[4]:


add(3,4)


# In[ ]:


#2. Passing arguments to a function:
   #Arguments can be passed to a function in Python either positionally or by keyword.
   #Positional arguments:** These are arguments passed to a function in the order they are defined. The function parameters receive the values based on their position. Example: `add(3, 5)`.
   #Keyword arguments:** These are arguments preceded by the parameter name during the function call. This allows for passing arguments out of order or specifying only some arguments. Example: `add(b=5, a=3)`.


# In[13]:


#3. Purpose of the return statement:#
   # The `return` statement is used to exit a function and return a value as the original type.
   #A function can have multiple `return` statements, but only one of them will be executed, after which the function exits.
   #Example:

   #python
def absolute_value(x):
    if x >= 0:
        return x
    else:
           return -x
   


# In[14]:



absolute_value(-5)


# In[16]:


#4. Lambda functions in Python:**
   #Lambda functions are small, anonymous functions defined using the `lambda` keyword.
   #They can have any number of arguments but can only have one expression.
   #They are often used when you need a short function for a short period of time.
   # Example:

   #python
double = lambda x: x * 2
print(double(5))  # Output: 10
   


# In[18]:


#5. Scope in Python:**
   #Scope refers to the visibility of variables within a program.
   #Local scope:** Variables defined within a function are scoped locally and are only accessible within that function.
   #Global scope:** Variables defined outside of any function are scoped globally and can be accessed from anywhere in the code.


# In[19]:


#6. Returning multiple values from a function:
 #  - You can use tuple packing to return multiple values from a function in Python.
  # - Example:

   #```python
def get_values():       
    return 1, 2, 3
a, b, c = get_values()
print(a, b, c)  # Output: 1 2 3
  


# In[20]:


#7. Pass by value vs. pass by reference:
  # - Python uses pass by object reference. When you pass a mutable object like a list or dictionary to a function, you are passing a reference to the object, so modifications made inside the function affect the original object.
   #- Immutable objects like integers, strings, and tuples are passed by value, meaning the function receives a copy of the object, and modifications made inside the function do not affect the original object.


# In[21]:


#8. Function for mathematical operations:
   
import math
def math_operations(x):
    return math.log(x), math.exp(x), pow(2, x), math.sqrt(x)
   


# In[22]:


math_operations(10)


# In[26]:


#9. Function to extract first name and last name from a full name:
   
def extract_names(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return first_name, last_name
   


# In[29]:


extract_names("Shubham Kumar Tiwari")


# In[ ]:




