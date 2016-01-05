#! /usr/bin/env python

def increment(password, index):
    # Provides the next password
    c = password[index]
    if c is not 'z':
        password = password[:index] + chr(ord(c) + 1) + password[index + 1:]
    else:
        password = password[:index] + 'a' + password[index + 1:]
        password = increment(password, index - 1)
    return password

def validate(password):
    # Validates the password
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    if not check_increasing_triplet(password):
        return False
    if not check_double_double(password):
        return False
    return True

def check_increasing_triplet(password):
    '''
    Checks if password contains an increasing triplet like 'abc'
    '''
    if len(password) < 3:
        return False
    current = 2
    while current < len(password):
        a, b, c = password[current - 2], password[current - 1], password[current]
        if ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c):
            return True
        current += 1
    return False

def check_double_double(password):
    '''
    Checks if the password has two couples of consecutive same charachters
    E.g., aaxbb
    '''
    if len(password) < 4:
        return False
    current = 1
    found = 0
    while current < len(password):
        a, b = password[current - 1], password[current]
        if a == b:
            found += 1
            current += 2
        else:
            current += 1
        if found == 2:
            return True
    return False

def part1(password):
    while not validate(password):
        password = increment(password, len(password) - 1)
    return password

def main():
    first = part1('cqjxjnds')
    print first
    print part1(increment(first, len(first) - 1))

if __name__ == '__main__':
    main()
