"""
Angel Zarate
Personal Project: Wordle Solver

This represents a current Game and all the potential words.
Initiate with a dictionary with all words in dictionary of length 5.
"""
"""TODO Find a word list that has all english words"""
import nltk
from nltk.corpus import words

class Game:

    def __init__(self, file_name):
        print("testing xd " + file_name)
        self.rand()
        dictionary = words.words()
        print(len(dictionary))

    def rand(self):
        print("inside Game > Rand")
