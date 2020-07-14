#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:13:47 2020

@author: michelle
"""


a = 4306
b = 8612

Oddtotal = 0
for number in range(a,(b+1)): 
    if(number % 2 == 1):
        Oddtotal = Oddtotal + number

print(Oddtotal)
    