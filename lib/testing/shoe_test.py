#!/usr/bin/env python3

from shoe import Shoe

import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        
    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
       
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        
       
        
        
   
