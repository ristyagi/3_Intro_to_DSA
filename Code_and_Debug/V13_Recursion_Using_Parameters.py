#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  29 22:12:27 2025

@author: Rishabh_Tyagi
"""

"""
Credits : https://www.youtube.com/@codeanddebug
https://www.youtube.com/watch?v=fgurDxhawRw&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=15

DSA Python Course 2025 - Recursion Using Parameters - Part 13 [Hindi] | Code & Debug
"""


##### print x, n times using recursion #####

def print_func(x, n):
    if n == 0:
        return
    print(x)
    print_func(x, n-1) # recursion fn call, so that next iteration is called with n-1

print_func(15,4)
