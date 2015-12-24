#! /usr/bin/env python

def transform(sequence):
    if len(sequence) == 1:
        return "1" + sequence
    consecutives = 1
    output = ""
    index  = 1
    while index < len(sequence):
        if sequence[index] == sequence[index - 1]:
            consecutives += 1
        else:
            output += str(consecutives) + sequence[index - 1]
            consecutives = 1
        index += 1
    output += str(consecutives) + sequence[index - 1]
    return output


# Output for part 2
def main():
    out = "1113222113"
    for _ in range(50):
        out = transform(out)
    print len(out)

if __name__ == '__main__':
    main()
