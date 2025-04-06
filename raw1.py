import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        lines.append(s[::-1] + s[1:])

    width = len(lines[0])
    for i in range(size-1, 0, -1):
        print(lines[i].center(width, '-'))
    for i in range(size):
        print(lines[i].center(width, '-'))

print_rangoli(5)