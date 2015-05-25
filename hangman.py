from random import randint


def hangman_game():
    chosen_word = random_word()
    print chosen_word


def random_word():
    f = open('words.txt', 'r')
    words = f.read().split('\n')
    f.close()

    return words[randint(0, len(words) - 1)]
