#!/usr/bin/env python
# coding: utf-8

# In[44]:


import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    btw = book_to_words(book_url)
    lst = []
    maxSize = 0

    for i in btw:
        if len(i) > maxSize:
            maxSize=len(i)

    for j in btw:
        word = '_' * (maxSize - len(j))
        lst.append(str(j) + word)

    return radix_sort(btw, maxSize)

def radix_sort(words, maxSize):
    wordLst = []
    charLst = ''
    digit = 1

    for i in words:
        for j in i:
            charLst.join(ord(j))
        wordLst.append(charLst)
        charLst = ''

    while(maxSize / digit > 0):
        counting_sort(wordLst, digit)
        digit *= 10

def counting_sort(lst, digit):
    f = [0] * (len(lst))
    c = [0] * (len(lst))
    for i in range(len(lst)):
        c[(lst[i] // digit) % 10] += 1

    for j in range(len(lst)):
        c[j] += c[j - 1]

    x = len(lst) - 1
    while(x >= 0):
        f[c[(lst[x] // digit) % 10] - 1] = lst[x]
        c[(lst[x] // digit) % 10] -= 1
        i -= 1

    for y in range(len(lst)):
        lst[y] = f[y]


# In[ ]:
