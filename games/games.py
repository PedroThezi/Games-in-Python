import guessing
import hangman
def choosing():
    while True:
        print('Do you wanna play a game?')
        print('1 - Guessing Game')
        print('2 - Hangman')
        print('0 - Quit')
        op = int(input('Pick a game: '))
    
        match op:
            case 1:
                guessing.play()
            case 2:
                hangman.play()
            case 0:
                print("Quiting...")
                break
            case _:
                print("Choose a valid option!")

if __name__ == "__main__":
    choosing()