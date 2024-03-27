#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Q.1
import keyword

print(keyword.kwlist)


# In[ ]:



# Q.2
# Rules to create variables in Python:
# - Variable names must start with a letter (a-z, A-Z) or underscore (_).
# - The rest of the variable name may consist of letters, numbers, and underscores.
# - Variable names are case-sensitive.
# - Variable names cannot be a Python keyword.
# - Variable names should be descriptive, conveying the meaning or purpose of the variable.


# In[ ]:



# Q.3
# Standards and conventions for variable naming in Python:
# - Use descriptive names that convey the purpose of the variable.
# - Use lowercase letters with words separated by underscores for improved readability (snake_case).
# - Avoid using single-character names except for counters or iterators.
# - Variable names should be nouns or noun phrases.
# - Constants should be named with all capital letters and underscores separating words (e.g., MAX_SIZE).


# In[ ]:



# Q.4
# If a keyword is used as a variable name, it will result in a syntax error because keywords are reserved for specific purposes and cannot be used for naming variables or other identifiers.


# In[ ]:


# Q.5
# The def keyword in Python is used to define a function.


# In[ ]:


# Q.6
# The special character '\' in Python is used as an escape character. It is used to indicate that the next character following it should be treated differently. For example, '\n' represents a newline character, '\t' represents a tab character.


# In[ ]:



# Q.7
# Examples:
# (i) Homogeneous list: [1, 2, 3, 4, 5]
# (ii) Heterogeneous set: {1, 'hello', 3.14, True}
# (iii) Homogeneous tuple: (1, 2, 3, 4, 5)


# In[ ]:


# Q.8
# Mutable and Immutable Data Types:
# - Mutable: Objects whose value can be changed after creation are mutable. Examples include lists, dictionaries, and sets.
# - Immutable: Objects whose value cannot be changed after creation are immutable. Examples include strings, tuples, and numeric types (int, float).

#example of mutable data type 
my_list = [1, 2, 3]
my_list[0] = 5
print(my_list)  # Output: [5, 2, 3]

# examples of immutable data type
my_tuple = (1, 2, 3)
# Attempting to modify the tuple will raise an error
# my_tuple[0] = 5  # This will raise a TypeError


# In[7]:


#Q.9
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))


# In[6]:


#Q.10
n = 5
i = n
while i >= 1:
    print(" "*(n-i) + "|"*(2*i-1))
    i -= 1


# In[ ]:




