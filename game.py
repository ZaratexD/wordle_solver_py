"""
Angel Zarate
Personal Project: Wordle Solver

This represents a current Game and all the potential words.
Initiate with a dictionary with all words in dictionary of length 5.
"""
"""TODO Find a word list that has all english words"""


class Game:

    def __init__(self, file_name):

        with open(file_name) as f:
            words = f.readlines()

            # self._word_dict = {k = word, v = num of repeated words}
            self._word_dict = {}

            for word in words:
                word = word.strip()
                if len(word) == 5:
                    self._word_dict[word] = self.num_of_repeated(word)


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

    # narrows down dictionary for words that dont fit criteria according to new_word
    def add_word(self, new_word):
        # new_word list of tupules
        # ex: [(t, grey), (e, yellow), (s, green), (t, grey)]

        # i can predict a lot of redundancy from initializer (scanning throw dict etc)
        print(str(self._word_dict))
        print(str(len(self._word_dict)))
        print()

        ### TODO SEPERATE DICTIONARY KEYS INTO OWN LIST (cannot modify dict while itterating)
        for i in range(len(new_word)):
            letter = new_word[i][0]
            color = new_word[i][1]
            keys = self._word_dict.keys()
            if color == "green":
                # key is a str ? and im using it as a list key[i]
                for key in keys:
                    if key[i] != letter:
                        print(key)
                        print(str(i) + " " + key[i] + letter)
                        #self._word_dict.pop(key)

            #elif color == "yellow":
            #    for key in keys:
            #        if letter not in key:
            #            print(key)
                        #self._word_dict.pop(key)
            # dont need this last one because first two take care of it (dic shouldnt have grey letter words)
            # elif color == "grey":
            #    pass

