def play():
    from random import randrange
    num = randrange(1,101)
    print('Try to guess a number between 1 and 100! You have 5 rounds')
    round = 0
    while round < 5:
        round += 1
        user = int(input(f'Round {round} Pick a number: '))
        if 0 < user < 101:
            pass
        else:
            continue
        if user == num:
            print(f'You got it!! in {round} tries')
            break
        elif user < num:
            print(f'Wrong! the number is bigger than {user}')
        else:
            print(f'Wrong! the number is lower than {user}')
    if round == 5:
        print(f'The number was {num}...')
    print('END!')

if (__name__ == "__main__"):
    play()
