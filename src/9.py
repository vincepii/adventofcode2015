#! /usr/bin/env python

import sys
import re

input = '''
Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70
'''

# E.g.: {'A': {'B': 100, 'C': 200},
#         'B': {'D': 150}
#        }
distances = {}

# E.g.: A, B, C
locations = set()

def shortest(points):
    '''
    points is a list of destinations, computes the shortest path to traverse
    all the points
    '''
    if len(points) < 2:
        raise Exception("Cannot travel to less than two places")
    if len(points) == 2:
        return distances.get(points[0]).get(points[1])
    min_distance = sys.maxint
    combs = combine(points)
    for comb in combs:
        total = 0
        for index in range(1, len(comb)):
            total += distances[comb[index - 1]][comb[index]]
        if total < min_distance:
            min_distance = total
    return min_distance

def longest(points):
    '''
    points is a list of destinations, computes the shortest path to traverse
    all the points
    '''
    if len(points) < 2:
        raise Exception("Cannot travel to less than two places")
    if len(points) == 2:
        return distances.get(points[0]).get(points[1])
    max_distance = 0
    combs = combine(points)
    for comb in combs:
        total = 0
        for index in range(1, len(comb)):
            total += distances[comb[index - 1]][comb[index]]
        if total > max_distance:
            max_distance = total
    return max_distance

def combine(points):
    '''
    Given a list of points returns all the dispositions of them as a list of
    lists
    '''
    res = []
    if len(points) == 1:
        res.append(points)
        return res
    if len(points) == 2:
        res.append([points[0], points[1]])
        res.append([points[1], points[0]])
        return res
    for index in range(len(points)):
        l = points[:index]
        l.extend(points[index + 1:])
        combs = combine(l)
        for comb in combs:
            comb.append(points[index])
            res.append(comb)
    return res

def parse_input():
    for line in input.split('\n'):
        if line == '':
            continue
        match = re.match('^(.*)\sto\s(.*)\s=\s([0-9]+)$', line)
        point1, point2, distance = match.group(1), match.group(2), int(match.group(3))
        if distances.get(point1) is None:
            distances[point1] = {}
        distances[point1][point2] = distance
        if distances.get(point2) is None:
            distances[point2] = {}
        distances[point2][point1] = distance
        locations.add(point1)
        locations.add(point2)

def main():
    parse_input()
    print shortest(list(locations))
    print longest(list(locations))

if __name__ == '__main__':
    main()
