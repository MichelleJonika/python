#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:37:51 2020

@author: michelle
"""

i = 1
f = open('rosalind_ini5.txt')
for line in f.readlines():
    if i % 2 == 0:
        print (line)
    i += 1