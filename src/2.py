input = """
10x9x8
"""

import re

total_paper = 0
total_ribbon = 0

for line in input.split():
    match = re.match("^([0-9]+)x([0-9]+)x([0-9]+)$", line)
    w,l,h = int(match.group(1)), int(match.group(2)), int(match.group(3))
    s1 = w * l
    s2 = w * h
    s3 = l * h
    area = 2 * s1 + 2 * s2 + 2 * s3 + min(s1, s2, s3)
    total_paper += area

    sides = [w,l,h]
    sides.sort()
    small_side1, small_side2 = sides[0], sides[1]
    total_ribbon += small_side1 * 2 + small_side2 * 2
    total_ribbon += w * l * h

print total_paper
print total_ribbon
