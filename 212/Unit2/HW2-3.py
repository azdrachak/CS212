# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

import itertools as itr

def is_palindrome(string):
    return True if string == string[::-1] else False

def longest_subpalindrome_slice(text):
    """Return (i, j) such that text[i:j] is the longest palindrome in text."""
    txt = str(text).lower()
    curr_pal = ''
    start = 0
    end = 0
    for i in range(len(txt)+1):
        for j in range(i, len(txt)+1):
            iter_pal = txt[i: j]
            if len(curr_pal) < len(iter_pal):
                if is_palindrome(iter_pal):
                    if len(curr_pal) < len(iter_pal):
                        curr_pal = iter_pal
                        start = i
                        end = j
    return start, end


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()