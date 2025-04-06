import random

while True:
    choice = input("ROLL THE DICE (Y/N): ").lower()
    if choice =='y':
        d1=random.randint(1,6)
        d2=random.randint(1, 6)
        print(f'({d1} {d2})')
        continue
    elif choice =='n':
        print("Thanks For Playing ")
        break
    else:
        print("INVALID CHOICE")