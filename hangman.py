from random import randint


def hangman_game():
    num_guesses = 7
    guessed_letters = 0
    guesses = []
    waiting_for_guess = True

    chosen_word = random_word()

    while num_guesses > 0 and guessed_letters is not len(chosen_word):
        while waiting_for_guess is True:
            guess = raw_input("Enter a letter: ")
            if len(guess) is not 1 or type(guess) is int:
                print "Invalid input, please try again"
            else:
                if guess not in chosen_word:
                    print guess + " is not in word"
                    num_guesses -= 1
                elif guess in guesses:
                    print guess + " has already been guessed"
                    num_guesses -= 1
                else:
                    print guess + " found in word"
                    for letter in chosen_word:
                        if letter is guess:
                            guessed_letters += 1
                waiting_for_guess = False
                guesses.append(guess)
        for letter in chosen_word:
            if letter in guesses:
                print letter,
            else:
                print "_",
        print "\n"
        waiting_for_guess = True
        print "Number of lives: " + str(num_guesses)

    if guessed_letters is len(chosen_word):
        print "Congratulations, you guessed the word correctly!"
    else:
        print "Game over!"


def random_word():
    f = open('words.txt', 'r')
    words = f.read().split('\n')
    f.close()

    return words[randint(0, len(words) - 1)]
