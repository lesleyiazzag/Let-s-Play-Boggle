"""Implements the logic of the game of boggle."""

from graphics import GraphWin
from boggleboard import BoggleBoard
from boggleletter import BoggleLetter
from brandom import randomize

class BoggleGame:

    __slots__ = [ "_validWords", "_board", "_foundWords", "_selectedLetters" ]

    def __init__(self, win):
        """
        Create a new Boggle Game and load in our lexicon.
        """
        # set up the set of valid words we can match
        self._validWords = self.__readLexicon()
        self._board = BoggleBoard(win)
        self._selectedLetters = []
        self._foundWords = []

        # init other attributes here.

    def __readLexicon(self, lexiconName='bogwords.txt'):
        """
        A helper method to read the lexicon and return it as a set.
        """
        validWords = set()
        with open(lexiconName) as f:
          for line in f:
            validWords.add(line.strip().upper())

        return validWords

    def doOneClick(self, point):
        """
        Implements the logic for processing one click.
        Returns True if play should continue, and False if the game is over.
        """
        # These steps are one way to think about the design, although
        # you are free to do things differently if you prefer.

        # step 1: check for exit button and return False if clicked
        if self._board.inExit(point):
            return False

        # step 2: check for reset button and reset
        elif self._board.inReset(point):
            self._board.reset()
            self._selectedLetters = []
            self._foundWords = []
            return True
        

        # step 3: check if click is on a cell in the grid
        elif self._board.inGrid(point):

            # get BoggleLetter at point
            boglet = self._board.getBoggleLetterAtPoint(point)
            boglet.setFillColor('powder blue')
            boglet.setTextColor('blue')

            # if this is the first letter in a word being constructed,
            # add letter and display it on lower text of board
            if len(self._selectedLetters) == 0:
                self._selectedLetters.append(boglet)
                self._board.setStringToLowerText(self._board.getStringFromLowerText() + boglet.getLetter())
            
            # else if clicked on same letter as last time, end word and check for validity
            elif boglet == self._selectedLetters[-1]: 
                bogletString = "".join([boglet.getLetter() for boglet in self._selectedLetters])
                if bogletString in self._validWords and bogletString not in self._foundWords:
                    self._foundWords.append(bogletString) # append to foundWords and side text of game
                    # Add every valid word that is found gradually to the side text of game
                    wordsString = '\n'.join(self._foundWords) 
                    self._board.setStringToTextArea(wordsString)
                self._board.resetColors() # clear lowertext, colors, and selectedLetters
                self._board.setStringToLowerText('')
                self._selectedLetters = []
                    
            # else if adding a letter to a non-empty word, make sure it's adjacent
            # and update state
            elif boglet.isAdjacent(self._selectedLetters[-1]) and boglet not in self._selectedLetters:
                self._selectedLetters.append(boglet)
                self._board.setStringToLowerText(self._board.getStringFromLowerText() + boglet.getLetter())
                # Set the last boggle letter clicked to green and set the current one clicked to blue
                self._selectedLetters[-2].setFillColor('light green')
                self._selectedLetters[-2].setTextColor('green')
                boglet.setFillColor('powder blue')
                boglet.setTextColor('blue')

            # else if clicked anywhere else, reset the state to an empty word.
            else:
                self._board.resetColors()
                self._board.setStringToLowerText('')
                self._selectedLetters = []

        # return True to indicate we want to keep playing
        return True

if __name__ == '__main__':

    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!

    win = GraphWin("Boggle", 400, 400)
    game = BoggleGame(win)
    keepGoing = True
    while keepGoing:
        point = win.getMouse()
        keepGoing = game.doOneClick(point)
