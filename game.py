"""
Angel Zarate
Personal Project: Wordle Solver

This represents a current Game and all the potential words.
Initiate with a dictionary with all words in dictionary of length 5.
"""
"""TODO Find a word list that has all english words"""


class Game:

    def __init__(self, file_name):
        xd = 123
        print("testing xd Filename: " + file_name)
        print()
        with open(file_name) as f:
            words = f.readlines()
            print("This is with List of words before reduction " + str(len(words)))
            print(str(words))
            word_dict = {}

            for word in words:
                word = word.strip()
                if len(word) == 5:
                    word_dict[word] = len(word)
            print(str(len(word_dict)))
            print(str(word_dict))
            """
            for word in words:
                if len(word) != 5:
                    print("Word removed: " + word + " " +str(len(word)))
                    words.remove(word)
            print("After " + str(len(words)))
            print(str(words))
            """

            # words = dict(words) eventually it will be more efficient to just have a dictionary
            # keys = word, v = how unique (#of repeated words)


    def num_of_repeated(self, word):
        print("inside Game > Rand")
