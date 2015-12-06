#! /bin/bash

input='''
turn off 660,55 through 986,197
turn off 341,304 through 638,850
'''

import re

ROWS = 1000
COLS = 1000

OFF = 0
ON = 1
TOGGLE = 2

class Grid(object):

    def __init__(self):
        super(Grid, self).__init__()
        self._grid = []
        for i in range(0, ROWS):
            self._grid.append([0 for j in range(0, COLS)])

    def change_light(self, x1, y1, x2, y2, action):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if action != TOGGLE:
                    self._grid[i][j] = action
                else:
                    self._grid[i][j] ^= 1

    def count_on(self):
        on = 0
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if self._grid[i][j] == ON:
                    on += 1
        return on

    # For part 2
    def change_bright(self, x1, y1, x2, y2, action):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if action == ON:
                    self._grid[i][j] += 1
                elif action == OFF:
                    if self._grid[i][j] > 0:
                        self._grid[i][j] -= 1
                else:
                    self._grid[i][j] += 2

    # For part 2
    def count_bright(self):
        bright = 0
        for i in range(0, ROWS):
            for j in range(0, COLS):
                bright += self._grid[i][j]
        return bright

def parse_command(cmd):
    if len(cmd) < 2:
        return
    action = TOGGLE
    if 'on' in cmd:
        action = ON
    elif 'off' in cmd:
        action = OFF
    match = re.search('([0-9]+),([0-9]+)\sthrough\s([0-9]+),([0-9]+)', cmd)
    x1 = match.group(1)
    y1 = match.group(2)
    x2 = match.group(3)
    y2 = match.group(4)
    return action, int(x1), int(y1), int(x2), int(y2)

def part1():
    g = Grid()
    for command in input.split('\n'):
        if len(command) < 2:
            continue
        action, x1, y1, x2, y2 = parse_command(command)
        g.change_light(x1, y1, x2, y2, action)
    return g.count_on()

def part2():
    g = Grid()
    for command in input.split('\n'):
        if len(command) < 2:
            continue
        action, x1, y1, x2, y2 = parse_command(command)
        g.change_bright(x1, y1, x2, y2, action)
    return g.count_bright()

if __name__ == '__main__':
    print part2()
