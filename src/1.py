s = """
()
"""
# This is just part2

floor = 0
index = 0

for a in s:
    if a == '(':
        floor += 1
        index += 1
    elif a == ')':
        floor -= 1
        index += 1
    if floor == -1:
        break

print index
