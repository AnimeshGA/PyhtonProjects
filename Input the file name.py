# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:02:16 2021

@author: Royal
"""

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))