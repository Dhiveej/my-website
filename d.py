


def fa(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

n = int(input("ENTER N: "))
r = int(input("ENTER R: "))
c = n - r

if r > n or r < 0:
    print("INVALID INPUT")
else:
    print(fa(n) / (fa(c) * fa(r)))

