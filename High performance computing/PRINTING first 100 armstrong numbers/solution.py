#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def is_armstrong(num):
    
    num_str = str(num)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == num

count = 0
number = 0

while count < 100:
    if is_armstrong(number):
        print(number)
        count += 1
    number += 1


# In[ ]:




