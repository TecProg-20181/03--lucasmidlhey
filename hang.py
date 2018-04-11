import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Message:

    def __init__ (self, guesses):
        self.guesses = guesses
        self.secretWord = self.loadWords()
        word = Word()
    def startMensseger(self):
        print ('Welcome to the game, Hangam!')
        print ('I am thinking of a word that is', len(self.secretWord), ' letters long.')
        print ('-------------')


class Word:

    def __init__ (self,guesses):
        self.guesses = guesses
        self.secretWord = self.loadWords()
        self.lettersGuessed = []
        self.availableLetters = string.ascii_lowercase

    def loadWords(self):

    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = string.split(line)
    print("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)

    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):
        guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        return guessed

    def availableWords(self):
        if self.isWordGuessed() ==False and self.guesses >0:
            return True
        else:
            return False


def hangman():
    guesses = 8
    word = Word(guesses)
    message = Message(guesses)

    message.startMensseger()

    while  word.availableWords()
        print ('You have ', guesses, 'guesses left.')

        for letter in availableLetters:
            if letter in lettersGuessed:
                word.availableLetters = word.availableLetters.replace(letter, '')

        print ('Available letters'), word.availableLetters

        letter = raw_input('Please guess a letter: ')
            if letter in word.lettersGuessed:
                print ('Oops! You have already guessed that letter: ', guessed)
            elif letter in word.secretWord:
                word.lettersGuessed.append(letter)
                print ('Good Guess: ', word.getGuessedWord())

        else:
            guesses -=1
            word.lettersGuessed.append(letter)
                print ('Oops! That letter is not in my word: ',  guessed)
                print ('------------')
        else:


hangman()
