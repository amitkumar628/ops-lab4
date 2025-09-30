#!/usr/bin/env python3

def first_five(s):
    """Return the first five characters of a string"""
    return s[:5]

def last_seven(s):
    """Return the last seven characters of a string"""
    return s[-7:]

def middle_number(num):
    """
    Return the middle digit(s) of a number.
    If even length, return the middle two digits.
    """
    s = str(num)
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid-1:mid+1]   # even length → two digits
    else:
        return s[mid]           # odd length → single digit

def first_three_last_three(s1, s2):
    """Combine the first 3 chars of s1 and last 3 chars of s2"""
    return s1[:3] + s2[-3:]

