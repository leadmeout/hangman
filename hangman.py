import random
from word_list import word_list as wl

#word_list = ['monkey', 'tiger', 'dragon']

#chosen_word = random.choice(word_list)


def hangman(chosen_word):

    chosen_word = chosen_word.lower()
    display = []
    lives = 6
    word_length = len(chosen_word)

    print(f"The word is: {chosen_word}")

    for _ in range(word_length):
        display += '_'
    
    print(" ".join(display))

    while True:

        if lives == 0:
            print("You ran out of lives; you lose!")

        guess = input("Please guess a letter: ").lower()

        if guess in chosen_word:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else: 
            lives -= 1

        print(" ".join(display))

        if "".join(display) == chosen_word:
            print("Congrats, you won!")
            break
        

hangman(random.choice(wl))