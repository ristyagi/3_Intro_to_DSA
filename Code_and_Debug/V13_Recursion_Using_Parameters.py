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

##### print 1 to n head recursion with two parameters #####
def func_print_n_two_param_head(i, n):
    if i>n:
        return
    print(i)                            # head recursion as action takes place before fn call
    func_print_n_two_param_head(i+1, n)
func_print_n_two_param_head(1,5)


##### print n to 1 tail recursion with two parameters #####
def func_print_n_two_param_tail(i, n):
    if i>n:
        return
    func_print_n_two_param_tail(i+1, n)
    print(i)                            # tail recursion as action takes place before fn call
func_print_n_two_param_tail(1,5)



##### print n to 1 head recursion with one parameter #####
def print_func(n):
    if n == 0:
        return
    print(n)
    print_func(n-1) # recursion fn call, so that next iteration is called with n-1
print_func(5)
