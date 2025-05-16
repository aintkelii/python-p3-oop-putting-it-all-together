#!/usr/bin/env python3

from book import Book

import io
import sys

class TestBook:
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
      
        
        

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        
    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        
