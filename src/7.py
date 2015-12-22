#! /usr/bin/env python

import re

input = '''
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''

DIRECT = 0
AND = 1
OR = 2
LSHIFT = 3
RSHIFT = 4
NOT = 5

op_to_enum = {'DIRECT': 0,
              'AND': 1,
              'OR': 2,
              'LSHIFT': 3,
              'RSHIFT': 4,
              'NOT': 5}

values = {}

class opdesc(object):

    def __init__(self, optype, lhs, rhs, dest):
        super(opdesc, self).__init__()
        self.optype = optype
        self.lhs = lhs
        self.rhs = rhs
        self.dest = dest

# Method to parse instruction
# Method to recursively resolve line

def _parse_doubleop(wiring):
    '''
    Parses the line describing an operation with two operands and returns
    the descriptor
    '''
    regex = '^(.+)\s(.+)\s(.+)\s->\s(.+)$'
    match = re.search(regex, wiring)
    lhs, op, rhs, dest = match.group(1), match.group(2), match.group(3), match.group(4)
    desc = opdesc(op_to_enum[op], lhs, rhs, dest)
    return desc

def _parse_unary(wiring):
    # NOT x -> h
    regex = '^(.+)\s(.+)\s->\s(.+)$'
    match = re.search(regex, wiring)
    op, lhs, dest = match.group(1), match.group(2), match.group(3)
    desc = opdesc(op_to_enum[op], lhs, None, dest)
    return desc

def _parse_assignment(wiring):
    # 123 -> x
    regex = '^(.+)\s->\s(.+)$'
    match = re.search(regex, wiring)
    lhs, dest = match.group(1), match.group(2)
    desc = opdesc(DIRECT, lhs, None, dest)
    return desc

def _parse_dest(wiring):
    '''
    Returns the destination operand of an operation
    '''
    regex = '^.*->\s(.+)$'
    match = re.search(regex, wiring)
    return match.group(1)

def findvalue(wire):
    '''
    Returns the value of a wire
    '''
    value = values.get(wire)
    if value is None:
        for connection in input.split('\n'):
            if len(connection) < 2:
                continue
            if _parse_dest(connection) == wire:
                parse_connection(connection)
    return values[wire]

def get_operand_value(operand):
    if operand.isdigit():
        return int(operand)
    return findvalue(operand)

def parse_connection(wiring):
    if 'AND' in wiring:
        desc = _parse_doubleop(wiring)
        lhs = get_operand_value(desc.lhs)
        rhs = get_operand_value(desc.rhs)
        values[desc.dest] = lhs & rhs
    elif 'OR' in wiring:
        desc = _parse_doubleop(wiring)
        lhs = get_operand_value(desc.lhs)
        rhs = get_operand_value(desc.rhs)
        values[desc.dest] = lhs | rhs
    elif 'LSHIFT' in wiring:
        desc = _parse_doubleop(wiring)
        lhs = get_operand_value(desc.lhs)
        rhs = get_operand_value(desc.rhs)
        values[desc.dest] = (lhs << rhs) & 0xFFFF
    elif 'RSHIFT' in wiring:
        desc = _parse_doubleop(wiring)
        lhs = get_operand_value(desc.lhs)
        rhs = get_operand_value(desc.rhs)
        values[desc.dest] = lhs >> rhs
    elif 'NOT' in wiring:
        desc = _parse_unary(wiring)
        lhs = get_operand_value(desc.lhs)
        values[desc.dest] = (~lhs) & 0xFFFF
    else:
        # Direct assignment
        desc = _parse_assignment(wiring)
        lhs = get_operand_value(desc.lhs)
        values[desc.dest] = lhs
    return desc

def main():
    print findvalue('e')

'''
For part 2:
just replace the assignment to b with
46065 -> b
and look again for the value of a
'''


if __name__ == '__main__':
    main()
