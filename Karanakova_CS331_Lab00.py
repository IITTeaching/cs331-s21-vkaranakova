#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_palindrome():
    return 'mom'


# In[2]:


def main():
    pal = my_palindrome()
    assert isinstance(pal, str), 'Must return a string'
    assert pal.strip(), 'String should not be empty'
    assert len(pal) > 1, 'String should be at least 2 letters long'
    assert pal == pal[::-1], 'String is not a palindrome'
    print("your successfully created a palindrome!")

if __name__ == '__main__':
    main()
    


# In[ ]:





# In[ ]:




