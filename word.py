import random
class Word:
    def __init__(self, word):
        self.word = word
        self.orderedLetters = word.split("")
    def checkValiditiy(self, listOfUnorderedConstraints, listOfOrderedContstraints):
        if(listOfUnorderedConstraints not in self.orderedLetters):
            return False
        for i in range(len(self.word)):
            if(listOfOrderedContstraints[i] != self.orderedLetters[i]):
                return False
        return True








