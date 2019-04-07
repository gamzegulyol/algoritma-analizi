#!/usr/bin/env python
# coding: utf-8

# In[1]:


def findMax(my_list):
    max=my_list[0]
    s=-1
    for i in range(len(my_list)):
        if(max<=my_list[i]):
            max=my_list[i]
            s=i
    return max,s

list_1=[1342245434,24124214,3,4,5,56,6,71,77,566,234,534,377,52,2768]
findMax(list_1)


# In[4]:


import random
def generate_numbers(n):
    numbers=[]
    for i in range(n):
        s=random.randint(0,100000000)
        numbers.append(s)
    return numbers

findMax(generate_numbers(10000000))


# In[8]:


import time
def recursive_fibonacci(n):
    if(n<2):
        return n
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)


# In[9]:


#fibo icin karmasılık 2^n dir.
for i in range(15):
    s=recursive_fibonacci(i)
    print(s,end=" ")


# In[ ]:


baslangic=time.time()
s=recursive_fibonacci(40)
print(s,end=" ")
bitis=time.time()
print("zaman=",bitis-baslangic)


# In[ ]:




