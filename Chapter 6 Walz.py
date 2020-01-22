#!/usr/bin/env python
# coding: utf-8

# Chapter 6 Walz
# Programmer:Gavin Walz
# Notes for Chapter 6

# In[1]:


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


# In[2]:


alien_0 = {'color': 'green', 'points': 5}


# In[3]:


alien_0 = {'color': 'green'}


# In[4]:


print(alien_0['color'])


# In[5]:


alien_0 = {'color': 'green', 'points': 5}


# In[6]:


new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# In[7]:


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# In[8]:


alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# In[9]:


alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# In[2]:


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


# In[3]:


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# In[4]:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


# In[5]:


print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")


# In[6]:


Gavin_info= {
    'first': 'Gavin',
    'last' : 'Walz',
    'age' : '15',
    'city' : 'Tea'
    }


# In[7]:


Data= {
    'Jerry': '12',
    'Tobin' : '3',
    'Bob' : '56',
    'Billy' : '8',
    'John' : '9'
    }


# In[8]:


print("Bob's favorite number is " +
    Data['Bob'].title() +
    ".")


# In[14]:


Glossary= {
    'String': 'Strings are anything encased in two quotation marks.',
    'Float' : 'Floats are numbers that have a decimal point.',
    'Int' : 'Intergers are numbers without a decimal point.',
    'Loop' : 'A loop is a group of text that repeats until stopped.',
    'List' : 'A list is a group of items that can be used as a variable.'
    }


# In[15]:


print(Glossary['Loop'].title())


# In[16]:


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }


# In[17]:


for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


# In[18]:


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


# In[19]:


for name in favorite_languages.keys():
    print(name.title())


# In[35]:


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
if name in friends:
    print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")


# In[20]:


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


# In[21]:


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# In[22]:


print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
        print(language.title())


# In[9]:


Rivers= {
    'Nile': 'Egypt',
    'Mississippi': 'U.S',
    'Amazon': 'Brazil',
    }

print('The Nile river runs through ' + (Rivers['Nile'].title()))


# In[23]:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'Jayrod':'python',
    'Adam': 'python'
    }
if name not in favorite_languages.keys():
    print(name.title(), 'please take our poll!')

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# In[25]:


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# In[29]:


aliens=[]

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# In[30]:


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# In[31]:


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# In[33]:


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




