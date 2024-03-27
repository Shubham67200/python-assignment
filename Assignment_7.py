#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
#and store the results in variables. Then print the data in the following format by calling the
#variables:
a= 5 
b= 10


# In[3]:


#addition
a+b


# In[8]:


#subtraction
s=a-b
#multiplicaton
m=a*b
#Division
D=a/b
print( s)
print(m)
print(D)


# In[9]:


# Q.2. Difference between Operators:

# (i) '/'' & '//'':
# - `/` is the division operator in Python, which returns the quotient of the division operation, including decimal points if necessary.
# - `//` is the floor division operator in Python, which returns the floor of the quotient, discarding any fractional part.

a = 10
b = 3
print(a / b)  # Output: 3.3333333333333335
print(a // b) # Output: 3


# In[10]:


# Q.2 (ii) `**` & `^`:
# - `**` is the exponentiation operator in Python, used to raise a number to a power.
# - `^` is the bitwise XOR operator in Python, used for bitwise exclusive OR operation.

a = 2
b = 3
print(a ** b)  # Output: 8
print(a ^ b)   # Output: 1


# In[11]:


# Q.3. Logical Operators:
# Python provides the following logical operators:
# - `and`: Returns True if both statements are true.
# - `or`: Returns True if one of the statements is true.
# - `not`: Returns True if the statement is false.


# In[12]:


# Q.4. Right Shift Operator and Left Shift Operator:
# - Right Shift Operator (`>>`): This operator shifts the bits of a number to the right by a specified number of positions. It effectively divides the number by 2 for each shift to the right.
# - Left Shift Operator (`<<`): This operator shifts the bits of a number to the left by a specified number of positions. It effectively multiplies the number by 2 for each shift to the left.

# Right Shift Operator example
x = 8
y = x >> 2  # Shifting right by 2 positions
print(y)    # Output: 2 (binary 100 shifted right by 2 gives 10)


# In[13]:


# Q.4 
#Left Shift Operator example
x = 2
y = x << 3  # Shifting left by 3 positions
print(y)    # Output: 16 (binary 10 shifted left by 3 gives 10000)



# In[14]:


# Q.5. Code to check if 10 is present in the list or not:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

if 10 in my_list:
    print("10 is present in the list.")
else:
    print("10 is not present in the list.")


# In[ ]:




