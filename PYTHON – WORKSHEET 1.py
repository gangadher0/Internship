#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 11. Write a python program to find the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))


# In[1]:


# 12. Write a python program to find whether a number is prime or composite.

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# In[2]:


# 13. Write a python program to check whether a given string is palindrome or not.
string = input("Enter a string: ")
if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")


# In[3]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.
from math import sqrt

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))

c = sqrt(a**2 + b**2)

print("The third side is", c)


# In[5]:


#15. Write a python program to print the frequency of each of the characters present in a given string.

string = input("Enter a string: ")
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency of each character in the string is:\n")
for key, value in freq.items():
    print(key, ":", value)


# In[ ]:




