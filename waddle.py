import csv
import random
import string


def get_mystery_word(m_list):
    """Gets a random word from m_list and returns it.

    Args:
        m_list (list): List of acceptable solution words.

    Returns:
        string: Random word from m_list.
    """
    random.seed()
    index = random.randint(0, len(m_list))
    return m_list[index]


def guess_word(m_word, g_list, guess=None):
    """With the mystery word, guesses what word it could be from the list
    Generates an array indicating:
    - X if letter is not in word
    - G if letter is in word and in the right place
    - Y if letter is in word but not in the right place

    Args:
        m_word (string): Mystery word
        guess (string): Optional word to guess instead of generating.
    """
    pass

def read_words(filename):
    """Reads a CSV file and returns a list of words.

    Args:
        filename (string): filename of csv file to parse.

    Returns:
        list: List of words in csv file.
    """
    w_list = []
    with open(filename, newline='') as fh:
        reader = csv.reader(fh, delimiter='\n')
        for r in reader:
            w_list.append(r[0])
    return w_list

def get_stats(word_list):
    
    # Build letter slot dictionary
    letter_results = {}
    for letter in string.ascii_lowercase:
        letter_results[letter] = [0,0,0,0,0] # Init blank letter
        for w in word_list:
            index = 0
            for l in w:
                if l == letter:
                    letter_results[letter][index] += 1
                index += 1

    # Print all letters
    print("## ALL STATS ##")
    for l in string.ascii_lowercase:
        print(l, letter_results[l])

    print("## GET BEST 5 LETTERS FOR EACH SLOT ##")
    slot_results = {}
    for i in range(5):
        temp_sort = sorted(letter_results.items(), key=lambda v:v[1][i], reverse=True)
        # print(temp_sort)
        print(temp_sort[0:5])
        


        # highest_amount = 0
        # highest_letter = ''
        # for l in string.ascii_lowercase:
        #     # print(letter_results[l][i])
        #     if letter_results[l][i] > highest_amount:
        #         highest_letter = l
        #         highest_amount = letter_results[l][i]
        # print(f"{i+1}: {highest_letter}: {highest_amount}")





    return letter_results

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
    mystery_list = read_words('mystery.csv')
    guess_list = read_words('guess.csv')
    print("Number of mystery words:", len(mystery_list))
    print("Number of guessable words:", len(guess_list))

    # Get stats
    get_stats(mystery_list)

    # m_word = get_mystery_word(mystery_list)
    # print("Word to guess: ", m_word)

    # Start of guessing
    # Step 1: Choose an optimal first word that 



    # result = guess_word(m_word, guess_list, guess="notes")

    