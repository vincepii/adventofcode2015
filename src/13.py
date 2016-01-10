#! /usr/bin/env python

import re
import sys

input = '''
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 81 happiness units by sitting next to Carol.
Alice would lose 42 happiness units by sitting next to David.
Alice would gain 89 happiness units by sitting next to Eric.
Alice would lose 89 happiness units by sitting next to Frank.
Alice would gain 97 happiness units by sitting next to George.
Alice would lose 94 happiness units by sitting next to Mallory.
Bob would gain 3 happiness units by sitting next to Alice.
Bob would lose 70 happiness units by sitting next to Carol.
Bob would lose 31 happiness units by sitting next to David.
Bob would gain 72 happiness units by sitting next to Eric.
Bob would lose 25 happiness units by sitting next to Frank.
Bob would lose 95 happiness units by sitting next to George.
Bob would gain 11 happiness units by sitting next to Mallory.
Carol would lose 83 happiness units by sitting next to Alice.
Carol would gain 8 happiness units by sitting next to Bob.
Carol would gain 35 happiness units by sitting next to David.
Carol would gain 10 happiness units by sitting next to Eric.
Carol would gain 61 happiness units by sitting next to Frank.
Carol would gain 10 happiness units by sitting next to George.
Carol would gain 29 happiness units by sitting next to Mallory.
David would gain 67 happiness units by sitting next to Alice.
David would gain 25 happiness units by sitting next to Bob.
David would gain 48 happiness units by sitting next to Carol.
David would lose 65 happiness units by sitting next to Eric.
David would gain 8 happiness units by sitting next to Frank.
David would gain 84 happiness units by sitting next to George.
David would gain 9 happiness units by sitting next to Mallory.
Eric would lose 51 happiness units by sitting next to Alice.
Eric would lose 39 happiness units by sitting next to Bob.
Eric would gain 84 happiness units by sitting next to Carol.
Eric would lose 98 happiness units by sitting next to David.
Eric would lose 20 happiness units by sitting next to Frank.
Eric would lose 6 happiness units by sitting next to George.
Eric would gain 60 happiness units by sitting next to Mallory.
Frank would gain 51 happiness units by sitting next to Alice.
Frank would gain 79 happiness units by sitting next to Bob.
Frank would gain 88 happiness units by sitting next to Carol.
Frank would gain 33 happiness units by sitting next to David.
Frank would gain 43 happiness units by sitting next to Eric.
Frank would gain 77 happiness units by sitting next to George.
Frank would lose 3 happiness units by sitting next to Mallory.
George would lose 14 happiness units by sitting next to Alice.
George would lose 12 happiness units by sitting next to Bob.
George would lose 52 happiness units by sitting next to Carol.
George would gain 14 happiness units by sitting next to David.
George would lose 62 happiness units by sitting next to Eric.
George would lose 18 happiness units by sitting next to Frank.
George would lose 17 happiness units by sitting next to Mallory.
Mallory would lose 36 happiness units by sitting next to Alice.
Mallory would gain 76 happiness units by sitting next to Bob.
Mallory would lose 34 happiness units by sitting next to Carol.
Mallory would gain 37 happiness units by sitting next to David.
Mallory would gain 40 happiness units by sitting next to Eric.
Mallory would gain 18 happiness units by sitting next to Frank.
Mallory would gain 7 happiness units by sitting next to George.
'''

hvalues = {}
participants = set()

def mutual_balance(a, b):
    return hvalues[a][b] + hvalues[b][a]

def happiness(arrangement):
    if len(arrangement) < 2:
        return None
    if len(arrangement) == 2:
        return mutual_balance(arrangement[0], arrangement[1])
    index = 1
    balance = mutual_balance(arrangement[-1], arrangement[0])
    while index < len(arrangement):
        balance += mutual_balance(arrangement[index - 1], arrangement[index])
        index += 1
    return balance

def parseline(line):
    regex = '^([a-zA-Z]+).*(gain|lose)\s([0-9]+).*\s([a-zA-Z]+)\.$'
    match = re.match(regex, line)
    first = match.group(1)
    sign = 1 if match.group(2) == 'gain' else -1
    value = int(match.group(3)) * sign
    second = match.group(4)
    if hvalues.get(first) is None:
        hvalues[first] = {}
    hvalues[first][second] = value
    participants.add(first)

def arrange(participants):
    if len(participants) == 0:
        return None
    if len(participants) == 2 or len(participants) == 3:
        return [list(participants)]
    participants = list(participants)
    last = participants.pop(-1)
    newarrangements = []
    for arrangement in arrange(participants):
        for i in range(0, len(arrangement)):
            tmparr = arrangement[:i]
            tmparr.append(last)
            tmparr.extend(arrangement[i:])
            newarrangements.append(tmparr)
    return newarrangements

def computehighestarrangement(arrangements):
    maxh = sys.maxint * -1
    for arrangement in arrangements:
        score = happiness(arrangement)
        if score > maxh:
            maxh = score
    return maxh

def part1():
    arrangements = arrange(list(participants))
    print computehighestarrangement(arrangements)

def part2():
    me = "Vincenzo"
    participants.add(me)
    hvalues[me] = {}
    for subject in hvalues.keys():
        hvalues[subject][me] = 0
        hvalues[me][subject] = 0
    arrangements = arrange(list(participants))
    print computehighestarrangement(arrangements)

def main():
    for l in input.split('\n'):
        if len(l) == 0:
            continue
        parseline(l)
    part1()
    part2()

if __name__ == '__main__':
    main()
