#!/usr/bin/env python
# coding: utf-8

# In[10]:


#6-1 Person
'''
Programmer name: Drayzdin Thompson
Description: A Dictionary/Biography on Jennifer Thompson
'''

jennifer_Bio = {
    'first_name':'Jennifer',
    'last_name':'Thompson',
    'age':39,
    'city':'Tea',
}
print(jennifer_Bio)


# In[16]:


#6-2 Favorite Number
'''
Programmer name: Drayzdin Thompson
Description: A Dictionary of a select amount of peoples favorite number
'''
number_fav = {
    'Drayzdin':13,
    'Kellen':100,
    'Jarrod':13,
    'Jesse':214,
    'kyzek':6,
}
print('My favorite number is ' + str(number_fav['Drayzdin']))
print("Jarrod's favorite number is " + str(number_fav['Jarrod']))
print("Kellen's favorite number is " + str(number_fav['Kellen']))
print("kyzek's favorite number is " + str(number_fav['kyzek']))
print("Jesses favorite number is " + str(number_fav['Jesse']))


# In[19]:


# 6-3 Glossary
'''
Programmer name: Drayzdin Thompson
Description: A Dictionary that works as a glossary
'''
glossary = {
    'Boolean Logic' : 'Statement evaluates to true or false',
    'Conditional Statement':'if then statement',
    'Iterable': 'A property of collections that are used to provide elements one at a time and in sequence ',
    'Sliced':'Selecting a portion of a collection',
    'Concatenation':'Attaching two things side-by-side, frequently strings of text',
    'Tuple': 'A native type in python that can store a collection but cannot assign new values to individual elements ',
}

print('Boolean Logic: ' + glossary['Boolean Logic'] + '.')
print('Conditional Statement: ' + glossary['Conditional Statement'] + '.')
print('Iterable: ' + glossary['Iterable'] + '.')
print('Sliced: ' + glossary['Sliced'] + '.')
print('Tuple: ' + glossary['Tuple'] + '.')


# In[4]:


#6-4 Glossary_2
'''
Programmer name: Drayzdin Thompson
Description: A Dictionary that works as a glossary
'''
glossary_2 = {
    'Boolean Logic' : 'Statement evaluates to true or false',
    'Conditional Statement':'if then statement',
    'Iterable': 'A property of collections that are used to provide elements one at a time and in sequence ',
    'Sliced':'Selecting a portion of a collection',
    'Concatenation':'Attaching two things side-by-side, frequently strings of text',
    'Tuple': 'A native type in python that can store a collection but cannot assign new values to individual elements ',
    'namespace':'The set of variable and function names that have been reserved by the compiler/interpreter',
    'Arguments':'The values that the programmer provides in the function call',
    'Default Value':'The value of an argument if the function is called without that actual argument',
    'Iterable':'A property of collections that are used to provide elements one at a time and in sequence',
}

for keys, values in glossary_2.items():
    print("\n" + keys.title() + ': ' + values.title())


# In[6]:


#6-5 Rivers
'''
Programmer name: Drayzdin Thompson
Description: A Dictionary that lists a river and its location 
'''
river = {
    'Nile River':'Egypt',
    'Big Sioux River':'The US',
    'Congo River':'Africa',
}
for keys, values in river.items():
    print('The ' + keys + ' is located in ' + values)


# In[13]:


#6-6 Polling
'''
Programmer name: Drayzdin Thompson
Description: A Dictionary with a few people and their favorite language
'''
favorite_languages = {
    'Drayzdin':'python',
    'Kellen': " ",
    'Jesse':'Python',
}
for keys, values in favorite_languages.items():
    if values == " ":
        print(keys.title() + ' Please take the poll')
    else:
        print('Thank you for taking our poll ' + keys.title())


# In[20]:


#6-8 Pets
'''
Programmer name: Drayzdin Thompson
Description: Dictionaries filled with info on pets 
'''
herky = {'Species':'Shih tzu', 'Owner':'Jennifer'}
chewtle = {'Species':'Turtle', 'Owner':'Jerald'}
hunter = {'Species':'Golden Retriever', 'Owner':'Bob'}
rose = {'Species':'cat', 'Owner':'Sara'}
pets = [herky, chewtle, hunter, rose]

for pet in pets:
    for key, value in pet.items():
        print(key + ': ' + value)

