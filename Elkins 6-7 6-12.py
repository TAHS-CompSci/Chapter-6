#!/usr/bin/env python
# coding: utf-8

# In[51]:


"""
Fav_numbers_elkins.py
Adam Elkins
A dictionary listing the favorite numbers of my people.
"""

number= {
    'joe': ['4','3'],
    'karen': ['2','6'],
    'ozwald': ['0','1'],
    'evan': ['6','5']

}
for name, numbers in number.items():
    print(name.title() + "s favorite numbers are:")
    for number in numbers:
        print( number.title())


# In[53]:


print (number)


# In[ ]:




