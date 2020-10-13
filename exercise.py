#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:46:37 2020

@author: maurogaray
"""

def is_even(): 
    
    num = int(input("Please enter a number: "))    
    if ( num % 2 ) == 0:
        print( "This number  is even")
    

        
is_even()
#%%

def is_odd():
    
    num = int(input("Please enter a number: ")) 
    if ( num % 2 ) != 0: 
        print ( "This number  is odd")


is_odd() 