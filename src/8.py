#! /usr/bin/env python

import re

input = r'''
"azlgxdbljwygyttzkfwuxv"
"v\xfb\"lgs\"kvjfywmut\x9cr"
"merxdhj"
"dwz"
'''

RE_BS = r'\\\\'
RE_DQ = r'\\"'
RE_HX = r'\\x[0-9a-fA-F][0-9a-fA-F]'


def part1():
    total_raw = 0
    total_mem = 0
    for line in input.split('\n'):
        if line == '':
            continue
        total_raw += len(line)
        line = re.sub(RE_BS, 'a', line)
        line = re.sub(RE_DQ, 'a', line)
        line = re.sub(RE_HX, 'a', line)
        total_mem += (len(line) - 2)
    print total_raw - total_mem

def part2():
    total_raw = 0
    total_mem = 0
    for line in input.split('\n'):
        if line == '':
            continue
        total_raw += len(line)
        line = re.sub(r'\\', 'aa', line)
        line = re.sub(r'\"', 'aa', line)
        total_mem += len(line) + 2
    print total_mem - total_raw

def main():
    part2()

if __name__ == '__main__':
    main()
