import random

emojis = {
    'r': '✊',
    'p': '✋',
    's': '✂️'
}
choices = ('r', 'p', 's')


def decide_winner(player, computer):
    if player == computer:
        return "IT'S A TIE!"
    elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (
            player == 's' and computer == 'p'):
        return "YOU WIN!"
    else:
        return "COMPUTER WINS!"


while True:
    choice = input("ROCK, PAPER, OR SCISSORS (R/P/S): ").lower()
    if choice not in choices:
        print("INVALID CHOICE! PLEASE TRY AGAIN.")
        continue

    c1 = random.choice(choices)
    print(f'U CHOSE {emojis[choice]}')
    print(f'COMPUTER CHOSE {emojis[c1]}')

    result = decide_winner(choice, c1)
    print(result)

    b = input("CONTINUE? (Y/N): ").lower()
    if b == 'n':
        print("THANKS FOR PLAYING!")
        break
