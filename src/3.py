#! /usr/bin/env python

input="""
v^
"""

class Visited(object):

    def __init__(self):
        super(Visited, self).__init__()
        self._visited = set()
        self._current = (0,0)
        self._visited.add(self._current)

    def getnext(self, move):
        xshift = 0
        yshift = 0
        if move == '<':
            xshift = -1
        elif move == '>':
            xshift = 1
        elif move == '^':
            yshift = 1
        elif move == 'v':
            yshift = -1
        nx = (self._current[0] + xshift, self._current[1] + yshift)
        return nx

    def check(self, point):
        '''
        Returns 1 if the point had not been visited, 0 otherwise
        '''
        return 1 if point not in self._visited else 0

    def mark(self, point):
        '''
        Marks the point as visited
        '''
        self._visited.add(point)

    def move(self, point):
        '''
        Moves to this point
        '''
        self._current = point

def part1():
    visited = Visited()
    nvisited = 1
    for a in input:
        newhouse = visited.getnext(a)
        nvisited += visited.check(newhouse)
        visited.mark(newhouse)
        visited.move(newhouse)
    return nvisited

def part2():
    santa = Visited()
    robo = Visited()
    santavisited = 1
    robovisited = 0
    for index, a in enumerate(input):
        if index % 2 == 0:
            santahouse = santa.getnext(a)
            santavisited += santa.check(santahouse)
            santa.mark(santahouse)
            santa.move(santahouse)
            robo.mark(santahouse)
        else:
            robohouse = robo.getnext(a)
            robovisited += robo.check(robohouse)
            robo.mark(robohouse)
            robo.move(robohouse)
            santa.mark(robohouse)
    return santavisited + robovisited

if __name__ == '__main__':
    print part1()
    print part2()
