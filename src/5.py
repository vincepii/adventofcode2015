#! /bin/bash

input='''
'''

#### Part 1

vowels = 'aeiou'
excl_sq = ['ab', 'cd', 'pq', 'xy']

MIN_VOWELS = 3

def check_excluded_sq(char1, char2):
    sq = char1 + char2
    if sq in excl_sq:
        return True
    return False

def nice_string(string):
    '''
    Part 1 of day 5
    '''
    nvowels = 0
    ndoubles = 0
    if len(string) <= 1:
        return False
    previous = string[0]
    for nx in string[1:]:
        if previous in vowels:
            nvowels += 1
        if check_excluded_sq(previous, nx):
            return False
        if nx == previous:
            ndoubles += 1
        previous = nx
    # Check the last character
    if previous in vowels:
        nvowels += 1
    # We can stop the loop as soon as this is True
    if nvowels >= MIN_VOWELS and ndoubles >= 1:
        return True
    return False

def part1():
    nice = 0
    strings = input.split()
    for string in strings:
        if nice_string(string):
            nice += 1
    return nice

#### Part 2

def check_axa(string):
    '''
    Looks for the pattern axa in the string
    (two same letters interleaved by one letter)
    '''
    if len(string) < 3:
        return False
    c1, c3 = 0, 2
    while c3 < len(string):
        if string[c1] == string[c3]:
            return True
        c1 += 1
        c3 += 1
    return False

def check_doubles(string):
    '''
    Checks the repetition of any two consecutive chars
    '''
    if len(string) < 4:
        return False
    chars = string[0:2]
    if chars in string[2:]:
        return True
    else:
        return check_doubles(string[1:])

def part2():
    nice = 0
    strings = input.split()
    for string in strings:
        if check_axa(string) and check_doubles(string):
            nice += 1
    return nice

if __name__ == '__main__':
    print part2()
