#!/usr/bin/env python
# coding: utf-8

# Chapter 6 Hoffman Proggramer: Tobin Hoffman Notes for Chapter 6 dictionairies

# In[13]:


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


# In[14]:


alien_0 = {'color': 'green', 'points': 5}


# In[15]:


alien_0 = {'color': 'green'}


# In[16]:


alien_0 = {'color': 'green'}
print(alien_0['color'])


# In[17]:


alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# In[18]:


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# In[19]:


alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


# In[20]:


alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# In[21]:


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


# In[ ]:





# In[22]:


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# In[23]:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


# In[24]:


print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")


# In[25]:


tobin_info = {
    'first' : 'Tobin',
    'last' : 'Hoffman',
    'age' : '15',
    'city' : 'Tea',
    }


# In[26]:


print("tobins age is " +
    tobin_info['age'].title() +
    ".")


# In[27]:


print("Tobin lives in " +
    tobin_info['city'].title() +
    ".")


# In[28]:


data = {
    'jen': '18',
    'sarah': '69',
    'edward': '45',
    'phil': '420',
    'tom' : '666',
    }


# In[29]:


print("Sarah's favorite number is in " +
    data['sarah'].title() +
    ".")


# In[30]:


glossary = {
    'interger': 'Intergers are numbers without a decimal point.',
    'float': 'Floats are numbers a decimal point.',
    'string': 'Strings are anything incased in two quotation marks.',
    'loops': 'A loop is a group of words that repeat untill stopped.',
    'list' : 'A list is a list of items that can be used as a variable',
    }


# In[ ]:





# In[31]:


print(glossary['list'].title())


# In[32]:


user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}


# In[33]:


for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


# In[34]:


for k, v in user_0.items()


# In[35]:


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")


# In[36]:


for name in favorite_languages.keys():
    print(name.title())


# In[37]:


for name in favorite_languages:


# In[38]:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
        
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")


# In[39]:


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


# In[40]:


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


# In[41]:


print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    for language in favorite_languages.values():
        print(language.title())


# In[42]:


for language in set(favorite_languages.values()):
    print(language.title())


# In[43]:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# In[44]:


rivers = {
    'nile': 'Egypt',
    'mississippi': 'U.S.',
    'amazon': 'Brazil',
    }
print("The nile runs through " + (rivers['nile'].title()))


# In[45]:


polling = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'tommy': 'english',
    'jayrod' : 'spanish',
    
    }
if name not in polling.keys():
    print(name.title() +", Please take our poll.")
    
for name in sorted(polling.keys()):
    print(name.title() +",thank you for taking the poll.")


# In[46]:


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# In[51]:


# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
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


# In[52]:


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
    # Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# In[53]:


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


# In[55]:


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
    'Gwalz': {
        'first': 'Gavin',
        'last': 'Walz',
        'location': 'Accidnet',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# In[ ]:




