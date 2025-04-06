n = int(input("Enter a number: "))

if n == 1 or n == 0:
    print("NEITHER PRIME NOR COMPOSITE")
else:
    flag = True
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            flag = False
            break

    if flag:
        print("PRIME")
    else:
        print("NOT PRIME")

