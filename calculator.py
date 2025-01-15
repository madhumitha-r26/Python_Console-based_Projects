# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:35:04 2025

@author: Madhumitha
"""

first_no=int(input("ENTER 1ST NUMBER:"))
second_no=int(input("ENTER 2ND NUMBER:"))

o=input("CHOOSE THE OPTION:")

if(o=='+'):
    print(first_no+second_no)
elif(o=='-'):
    print(first_no-second_no)
elif(o=='*'):
    print(first_no*second_no)
elif(o=='%'):
    print(first_no%second_no)
elif(o=='/'):
    try:
        print(first_no//second_no)
    except ZeroDivisionError:
        print("CANNOT BE DIVIDED BY ZERO")
else:
    print("INVALID OPTION!")
