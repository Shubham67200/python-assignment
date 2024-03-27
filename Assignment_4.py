#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Q1: What exactly is []?
# A1: [] is an empty list in Python.
l=[]


# In[10]:


l


# In[16]:


# Q2: In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
# (Assume [2, 4, 6, 8, 10] are in spam.)
spam = [2, 4, 6, 8, 10]



# In[17]:


spam.insert(2,'hello')


# In[18]:


spam


# In[21]:


# Q3: What is the value of spam[int(int('3' * 2) / 11)]?
print(spam[int(int('3' * 2) / 11)])
# A3: spam[int(int('3' * 2) / 11)], the expression spam[int(int('3' * 2) / 11)] evaluates to  '6'.


# In[22]:


# Q4: What is the value of spam[-1]?
spam[-1]
# A4: The value of spam[-1] is the last element of the list spam, which is '10'.



# In[23]:


# Q5: What is the value of spam[:2]?
spam[:2]
# A5: The value of spam[:2] is a sublist of spam containing the elements up to, but not including, the element at index 2. So, it will be [2, 4]


# In[24]:


# Let's pretend the spam includes the list bacon = [3.14, 'cat', 11, 'cat', True] for the next three queries.
bacon = [3.14, 'cat', 11, 'cat', True]

# Q6: What is the value of bacon.index('cat')?
bacon.index('cat')
# A6: bacon.index('cat') returns the index of the first occurrence of 'cat' in the list bacon. Since it appears at index 1, the return value is 1.


# In[5]:


# Q7: How does bacon.append(99) change the look of the list value in bacon?
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99)
# A7: bacon.append(99) adds the value 99 to the end of the list bacon, so the list becomes [3.14, 'cat', 11, 'cat', True, 99].


# In[6]:


bacon


# In[7]:


# Q8: How does bacon.remove('cat') change the look of the list in bacon?
bacon.remove('cat')
# A8: bacon.remove('cat') removes the first occurrence of 'cat' from the list bacon, so the list becomes [3.14, 11, 'cat', True].


# In[8]:


bacon


# In[ ]:


# Q9: What are the list concatenation and list replication operators?
# A9: The list concatenation operator is +, and the list replication operator is *.

# Q10: What is difference between the list methods append() and insert()?
# A10: append() adds an element to the end of a list, while insert() inserts an element at a specified index.

# Q11: What are the two methods for removing items from a list?
# A11: The two methods for removing items from a list are remove() and pop(). remove() removes the first occurrence of a specified value, while pop() removes the element at a specified index.

# Q12: Describe how list values and string values are identical.
# A12: Both list values and string values are ordered collections of items. They both support indexing, slicing, concatenation, and repetition.

# Q13: What's the difference between tuples and lists?
# A13: Tuples and lists are both ordered collections of items, but lists are mutable (can be changed), whereas tuples are immutable (cannot be changed).

# Q14: How do you type a tuple value that only contains the integer 42?
# A14: To create a tuple value containing only the integer 42, you would type (42,). The comma is necessary to distinguish it from a mathematical expression in parentheses.

# Q15: How do you get a list value's tuple form? How do you get a tuple value's list form?
# A15: To convert a list value to a tuple, you can use the tuple() function. To convert a tuple value to a list, you can use the list() function.

# Q16: Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# A16: Variables that "contain" list values actually contain references to the list objects in memory.

# Q17: How do you distinguish between copy.copy() and copy.deepcopy()?
# A17: copy.copy() performs a shallow copy of a list, meaning it creates a new list object but does not recursively clone nested objects. 
# copy.deepcopy() performs a deep copy, creating a new list object as well as recursively copying all nested objects within it.

