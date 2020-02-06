#!/usr/bin/env python
# coding: utf-8

# In[2]:


alien_0= {'color': 'green', 'points': 5}


# In[3]:


print(alien_0['color'])


# In[4]:


new_points = alien_0['points']


# In[5]:


print("You just earned " + str(new_points)+ "points!")


# In[6]:


alien_0['x_position'] = 0
alien_0['y_position'] = 25


# In[7]:


print(alien_0)


# In[8]:


alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5


# In[9]:


print(alien_0)


# In[10]:


alien_0 = {'color': 'green'}


# In[11]:


print("The alien is " + alien_0['color'] + ".")


# In[12]:


alien_0['color'] = 'yellow'


# In[13]:


print("The alien is now " + alien_0['color'] + ".")


# In[15]:


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}


# In[16]:


print("Original x-position: " + str(alien_0['x_position']))


# In[18]:


if alien_0['speed'] == 'slow':
    x_incremennt = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_0['x_position'] = alien_0[]


# In[19]:


print("New x-position: " + str(alien_0['x_position']))


# In[1]:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


# In[3]:


print("Sarah's favorite language is " + 
     favorite_languages['sarah'].title() +
     ".")


# In[4]:


favorite_languages['sarah']


# In[12]:


friend = {'first_name': 'Adam', 'last_name': 'Elkins', 'age': 14, 'city': 'souix falls'}


# In[18]:


print(friend['first_name'])


# In[25]:


print(friend['first_name'] + " is", + (friend['age']))


# In[26]:


number = {'Adam': 92, 'Jarod': 72, 'Noah': 4, 'Jessie': 214, 'Gavin': 42}


# In[27]:


print(number['Adam'])


# In[29]:


print('Adams favorite number is', + (number['Adam']))


# In[30]:


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}


# In[31]:


for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


# In[33]:


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
         language.title() + ".")


# In[34]:


for name in favorite_languages.keys():
    print(name.title())


# In[36]:


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
             ", I see your favorite language is " +
             favorite_languages[name].title() + "!")
        
        


# In[37]:


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


# In[40]:


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# In[42]:


print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# In[ ]:




