#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1: What does an empty dictionary's code look like?
# A1: An empty dictionary is represented by curly braces with no key-value pairs inside.
empty_dict = {}


# In[2]:


# Q2: What is the value of a dictionary value with the key 'foo' and the value 42?
# A2: The value is 42.
dictionary = {'foo': 42}


# In[3]:


# Q3: What is the most significant distinction between a dictionary and a list?
# A3: The most significant distinction is that a dictionary stores key-value pairs, whereas a list stores ordered collections of items accessed by index.


# In[4]:


# Q4: What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# A4: You will get a KeyError because 'foo' is not a key in the dictionary spam.
spam = {'bar': 100}
# spam['foo']  # This will raise a KeyError


# In[5]:


# Q5: If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# A5: Both expressions check if 'cat' is a key in the dictionary. They are functionally equivalent.


# In[7]:


# Q6: If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# A6: 'cat' in spam checks if 'cat' is a key in the dictionary, while 'cat' in spam.values() checks if 'cat' is a value in the dictionary.



# In[8]:


# Q7: What is a shortcut for the following code?
#    if 'color' not in spam:
#        spam['color'] = 'black'
# A7: The setdefault() method can be used as a shortcut.
spam = {'bar': 100}
spam.setdefault('color', 'black')


# In[9]:


# Q8: How do you "pretty print" dictionary values using which module and function?
# A8: You can "pretty print" dictionary values using the pprint module and pprint() function.
import pprint
example_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
pprint.pprint(example_dict)


# In[ ]:




