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
            self._board.setStringToUpperText("")
            return True
        

        # step 3: check if click is on a cell in the grid
        elif self._board.inGrid(point):

          # get BoggleLetter at point
          boglet = self._board.getBoggleLetterAtPoint(point)

          # if this is the first letter in a word being constructed,
          # add letter and display it on lower text of board
          if len(self._selectedLetters) == 0:
              self._selectedLetters.append(boglet)
              self._board.setStringToLowerText(boglet.getLetter())
        return True

          # else if adding a letter to a non-empty word, make sure it's adjacent
          # and update state

          # else if clicked on same letter as last time, end word and check for validity

          # else if clicked anywhere else, reset the state to an empty word.

        # return True to indicate we want to keep playing

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
