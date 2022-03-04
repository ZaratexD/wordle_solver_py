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
                    word_dict[word] = self.num_of_repeated(word)
            print(str(len(word_dict)))
            print(str(word_dict))
            print()

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
        count = 0
        word = list(word)
        # print(str(word))
        # print(word[1])
        # this is gonna be O^2 can make it less run time by remove letters as i say redundancy but double redundancy?
        # applies to 5 letter words?
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                if word[i] == word[j]:
                    count += 1
        return count

