#!/usr/bin/env python
# coding: utf-8

# Chapter 6 Walz
# Programmer:Gavin Walz
# Notes for Chapter 6

# In[1]:


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    'htobin': {
        'first': 'Tobin',
        'last': 'Hoffman',
        'location': 'Accidnet'
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# In[ ]:




