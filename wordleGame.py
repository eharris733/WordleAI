#Created by Elliot Harris, April 18th, 2022

#list of all valid guesses: https://github.com/tabatkins/wordle-list/blob/main/words
import random
import re

class Word:
    def __init__(self, word):
        self.word = word
        self.orderedLetters = list(word)
        #bug in this function, or in the adding function to our lists
    def checkValiditiy(self, listOfUnorderedConstraints, listOfOrderedContstraints, listOfNotIncluded):
        for i in range(len(self.word)):
            if(self.orderedLetters[i] in listOfNotIncluded):
                return False
            if (listOfUnorderedConstraints[i]!= '' and listOfUnorderedConstraints[i] not in self.orderedLetters ):
                return False
            if (listOfUnorderedConstraints[i] == self.orderedLetters[i]):
                return False
            if(listOfOrderedContstraints[i] != '' and listOfOrderedContstraints[i] != self.orderedLetters[i]):
                return False
        return True


class WordleGame:
    def __init__(self, word, completeWords):
        self.word = Word(word)
        self.completeWords = completeWords
        self.guesses = 0
        self.correctGuess = False
        self.lettersIncluded = ['', '', '', '', ''] #problematic beacuse we have more than 5 constraints sometimes
        self.orderedLetters = ['', '', '', '', '']
        self.lettersNotIncluded = []
    def randomConstraintGuesser(self):
        guess = random.choice(self.completeWords)
        possibleWords = self.completeWords
        possibleGuesses = set()
        for i in range(6): #we have 6 guesses
            print('iteration ' + str(i + 1) + ' guess is ' + guess)
            if(guess == self.word.word):
                self.correctGuess = True
                print('correct guess! ' + self.word.word)
                return True
            else: #we get more info
                for c in range(len(guess)):
                    if guess[c] in self.word.orderedLetters and guess.find(guess[c]) == self.word.orderedLetters.index(guess[c]):
                        self.orderedLetters[guess.find(guess[c])] = guess[c]
                    elif(guess[c] in self.word.orderedLetters):
                        self.lettersIncluded[c] = guess[c]
                    else:
                        self.lettersNotIncluded.append(guess[c])

                for z in possibleWords:#need to remove the possibility of guessing the same thing again
                    tempWord = Word(z)
                    if(z == guess):
                        pass
                    if(tempWord.checkValiditiy(self.lettersIncluded, self.orderedLetters, self.lettersNotIncluded)):
                        print('added ' + str(z) + ' with ordered constraints ' + str(self.orderedLetters) + ' and unordered constraints ' + str(self.lettersIncluded))
                        possibleGuesses.add(z)
                if(len(possibleGuesses) == 0):
                    print('no possible Guesses to choose from')
                    return
                possibleWords = list(possibleGuesses)
                guess = random.choice(list(possibleWords))
                possibleGuesses.clear()

        print('Could not guess ' + str(self.word.word))
        return False
            #now we get a new guess
            #for w in self.completeWords:







global alphabetDict
alphabetDict = {}

#This loads the 10,000 or so words that are possible guesses in wordle from "betterwords.txt"
def loadEntireList(file):
    finalList = []
    with open(file, 'r') as words:
        for word in words.readlines():
            filteredWord = re.sub(r"[^a-z]", "", word.lower()) #should filter out everything but the alphabet numbers
            if(len(filteredWord) == 5):
                finalList.append(filteredWord)
    return finalList
#probably something off about this
def loadAnswerList(file):
    answerString = open(file, 'r').read()
    answerList = answerString.split(',')
    for i in range(len(answerList)):
        filteredWord = re.sub(r"[^a-z]", "", answerList[i].lower())
        if (len(filteredWord) == 5):
            answerList.append(filteredWord)
    return answerList


def frqTable(word):
    global alphabetDict
    for c in word:
        alphabetDict[c] = alphabetDict.get(c, 0) + 1

def main():
    masterList = loadEntireList("betterWords.txt")
    answerList = loadAnswerList("WordleAnswers.txt")
    # for word in answerList:
    #     wordleGame = WordleGame(word, masterList)
    #     wordleGame.randomConstraintGuesser()
    wordleGame = WordleGame(answerList[5], masterList)
    wordleGame.randomConstraintGuesser()
    #frqTable('think')


    #Where we run the various trials


if __name__ == '__main__':#Where we execute the code
    main()

