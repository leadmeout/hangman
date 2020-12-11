import random

#word_list = ['monkey', 'tiger', 'dragon']

#chosen_word = random.choice(word_list)



def hangman(chosen_word):

    chosen_word = chosen_word.lower()

    print(f"The word is: {chosen_word}.")

    display = []

    word_length = len(chosen_word)

    for _ in range(word_length):
        display += '_'
    
    print(" ".join(display))

    while True:

        guess = input("Please guess a letter: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(" ".join(display))

        if "".join(display) == chosen_word:
            print("Congrats, you won!")
            break
        

hangman("Marshmellow")