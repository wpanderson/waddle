from asyncore import read
import csv
import random


def get_mystery_word(m_list):
    """
    
    """
    random.seed()
    index = random.randint(0, len(m_list))
    return m_list[index]


if __name__ == '__main__':
    """
    Start of program

    Strategy:
    - Read in Wordle guessable words, read in wordle mystery words
    - Choose a random mystery word.
    - Choose a random word
    - Guess "notes"
    - continue guessing based on results
    """

    # Read in word lists
    mystery_list = []
    guess_list = []

    with open("mystery.csv", newline='') as fh:
        reader = csv.reader(fh, delimiter='\n')
        for r in reader:
            mystery_list.append(r[0])
    with open("guess.csv", newline='') as fh:
        reader = csv.reader(fh, delimiter='\n')
        for r in reader:
            guess_list.append(r[0])
    
    print("Number of mystery words:", len(mystery_list))
    print("Number of guessable words:", len(guess_list))

    m_word = get_mystery_word(mystery_list)
    print("Word to guess: ", m_word)
