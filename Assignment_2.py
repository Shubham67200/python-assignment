#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. What are the two values of the Boolean data type? How do you write them?
# The two values of the Boolean data type are True and False.

# 2. What are the three different types of Boolean operators?
# The three different types of Boolean operators are AND, OR, and NOT.

# 3. List of each Boolean operator's truth tables:
# AND truth table:
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

# OR truth table:
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False

# NOT truth table:
# not True  = False
# not False = True


# In[2]:



# 4. Values of the following expressions:
print((5 > 4) and (3 == 5))              # False
print(not (5 > 4))                        # False
print((5 > 4) or (3 == 5))                # True
print(not ((5 > 4) or (3 == 5)))          # False
print((True and True) and (True == False))# False
print((not False) or (not True))          # True

# 5. Six comparison operators:
# == (equal to)
# != (not equal to)
# >  (greater than)
# <  (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

# 6. Difference between equal to and assignment operators:
# The equal to operator (==) is used to compare two values to see if they are equal.
# Example: if x == y: 

# The assignment operator (=) is used to assign a value to a variable.
# Example: x = 10


# In[ ]:


# 7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')   # Block 1
if spam > 5:
    print('bacon')  # Block 2
else:
    print('ham')    # Block 3
print('spam')
print('spam')

# 8. Code that prints based on the value stored in spam:
spam = 2
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

# 9. If your program is stuck in an endless loop, you can press Ctrl + C to interrupt the execution.

# 10. Difference between break and continue:
# - break: Terminates the loop and transfers the execution to the statement immediately following the loop.
# - continue: Skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.

# 11. Difference between range(10), range(0, 10), and range(0, 10, 1):
# They all generate the same sequence of numbers from 0 to 9. The difference lies in their parameters:
# - range(10): Starts from 0 by default and ends at 9.
# - range(0, 10): Starts from 0 and ends at 9 explicitly specified.
# - range(0, 10, 1): Starts from 0, ends at 9, and increments by 1 (which is the default increment).

# 12. Program to print numbers 1 to 10 using a for loop:
for i in range(1, 11):
    print(i)

# Equivalent program using a while loop:
i = 1
while i <= 10:
    print(i)
    i += 1

# 13. Calling a function named bacon() inside a module named spam:
# If the function is defined as follows:
# def bacon():
#     print("Bacon function")
# Inside spam module, after importing spam, you can call the function as:
# spam.bacon()

