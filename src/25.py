#! /usr/bin/env python

def number_of_predecessors(x, y):
    '''
    Given a number at coordinates x, y, returns the number of predecessors
    of that number
    '''
    max_coord = x + y - 1
    full_triangle = max_coord - 1
    n = ((full_triangle * (full_triangle + 1)) / 2) + y - 1
    return n

def compute_number(x, y):
    pred = number_of_predecessors(x, y)
    number = 20151125
    for _ in range(pred):
        number = number * 252533
        number = number % 33554393
    return number

def main():
    print compute_number(2981, 3075)

if __name__ == '__main__':
    main()
