from random import randrange
def play():
    
    word = files()
    list_hit = ['_' for _ in word]
    print(list_hit)
    
    lost = False
    hit = False
    misses = 0
    tries = 7
    while(not lost and not hit):
        guess = input("Choose a letter:").upper().strip()
        if len(guess) != 1:
            continue

        if guess in word:
           check(guess,list_hit,word)
        else:
            misses += 1
            draw(misses)
            print(f'Wrong!, you have {tries - misses} tries left')
        
        lost = misses == tries
        hit = '_' not in list_hit
        print(list_hit)
    
    if hit:
        print("YOU WON!!!!")
    else:
        print('You lost...')
        print(f'The word was "{word}"')
    
    print("END!")

def files():
    words = []
    with open("words.txt",'r') as file:
        for row in file:
            row = row.strip()
            words.append(row)
    return words[randrange(0,len(words))].upper()

def check(guess,list_hit,word):
    index = 0
    for letter in word:
        if guess == letter:
            list_hit[index] = letter
        index += 1

def draw(misses):
    print("  _______     ")
    print(" |/      |    ")

    if(misses == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(misses == 2):
        print (" |      (_)   ")
        print (r" |      \     ")
        print (" |            ")
        print (" |            ")

    if(misses == 3):
        print (" |      (_)   ")
        print (r" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(misses == 4):
        print (" |      (_)   ")
        print (r" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(misses == 5):
        print (" |      (_)   ")
        print (r" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(misses == 6):
        print (" |      (_)   ")
        print (r" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (misses == 7):
        print (" |      (_)   ")
        print (r" |      \|/   ")
        print (" |       |    ")
        print (r" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    play()
