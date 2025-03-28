"""
Extends the Board class with specific features required for Boggle
"""

from graphics import *
from brandom import *
from boggleletter import BoggleLetter
from board import Board

class BoggleBoard(Board):
    """Boggle Board class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a grid
    of BoggleLetters, shaken appropriately to randomize play."""

    __slots__ = ['_grid', "_cubes"]

    def __init__(self, win):
        super().__init__(win, rows=4, cols=4)

        self._foundWords = []  # Track found words
        self._max_visible_words = 15  # Max number of words that can be visible at once
        self._scroll_position = 0

        self._cubes =  [[ "A", "A", "C", "I", "O", "T" ],
                        [ "T", "Y", "A", "B", "I", "L" ],
                        [ "J", "M", "O", "Qu", "A", "B"],
                        [ "A", "C", "D", "E", "M", "P" ],
                        [ "A", "C", "E", "L", "S", "R" ],
                        [ "A", "D", "E", "N", "V", "Z" ],
                        [ "A", "H", "M", "O", "R", "S" ],
                        [ "B", "F", "I", "O", "R", "X" ],
                        [ "D", "E", "N", "O", "S", "W" ],
                        [ "D", "K", "N", "O", "T", "U" ],
                        [ "E", "E", "F", "H", "I", "Y" ],
                        [ "E", "G", "I", "N", "T", "V" ],
                        [ "E", "G", "K", "L", "U", "Y" ],
                        [ "E", "H", "I", "N", "P", "S" ],
                        [ "E", "L", "P", "S", "T", "U" ],
                        [ "G", "I", "L", "R", "U", "W" ]]
 
        self._grid = [] #initializes empty list of lists
        for col in range(self._cols):
            grid_col = [] #iterate over each column to create the inner lists
            for row in range(self._rows): #for every instance of row in the columns
                letter = BoggleLetter(self.getBoard(), col, row) #create new boggle letter
                grid_col.append(letter) #add empty boggle letters to column
            self._grid.append(grid_col) #add column to the grid
        self.shakeCubes()
        
    def addFoundWord(self, word):
        """
        Add a found word to the list, update the text area, and trigger scroll functionality.
        """
        if word not in self._foundWords:
            self._foundWords.append(word)
        if len(self._foundWords) > self._max_visible_words:
            self._scroll_position += 1
        self.updateTextArea()

    def updateTextArea(self):
        """
        This method updates the text area to display the current found words list
        based on the scroll position.
        """
        # Get the words to display (consider scroll position)
        visible_words = self._foundWords[self._scroll_position:self._scroll_position + self._max_visible_words]

        # Join the words into a string
        wordsString = '\n'.join(visible_words)

        # Update the text area
        self.setStringToTextArea(wordsString)

    def scrollWordsUp(self):
        """
        Override the scroll behavior to update the text area with new words.
        """
        if self._scroll_position > 0:
            self._scroll_position -= 1
            self.updateTextArea() 

    def scrollWordsDown(self):
        """
        Scroll down the word list if the user scrolls down.
        """
        if self._scroll_position + self._max_visible_words < len(self._foundWords):
            self._scroll_position += 1
            self.updateTextArea() 

    def getBoggleLetterAtPoint(self, point):
        """
        Return the BoggleLetter that contains the given point in the window,
        or None if the click is outside all letters.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = BoggleBoard(win)
        >>> pointIn_0_0 = Point(board.getXInset() + board.getSize() / 2, \
                                board.getYInset() + board.getSize() / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_0_0) == board._grid[0][0]
        True
        >>> pointIn_1_2 = Point(board.getXInset() + board.getSize() * 3 / 2, \
                                board.getYInset() + board.getSize() * 5 / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_1_2) == board._grid[1][2]
        True
        >>> win.close()
        """
        # If we click inside of the grid... 
        if self.inGrid(point):
            (col, row) = self.getPosition(point)
            # retrieve the grid coordinates of the click
            return self._grid[col][row]
        else:
            return None

    def resetColors(self):
        """
        "Unclicks" all boggle letters on the board without changing any
        other attributes.  (Change letter colors back to default values.)
        """
        # Go through every square on the grid and reset text and square colors to default.
        for col in self._grid:
            for row in col:
                row.setTextColor('black')
                row.setFillColor('white')

    def reset(self):
        """
        Clears the boggle board by clearing letters and colors,
        clears all text areas (right, lower, upper) on board
        and resets the letters on board by calling shakeCubes.
        """
        # Reset colors, clear all text areas, and shake the cubes for a new pattern.
        self.resetColors()
        self._foundWords = [] 
        self._scroll_position = 0
        self.setStringToTextArea('')
        self.setStringToUpperText('')
        self.setStringToLowerText('')
        self.shakeCubes()

    def shakeCubes(self):
        """
        Shakes the boggle board and sets letters as described by the handout.
        """
        faceList = []
        # Shuffle the lists representing cubes in the list of lists self._cubes
        shuffledVersion = shuffled(self._cubes)
        # Iterating through each die
        for dieList in shuffledVersion:
            # Call a random face for each die
            face = dieList[randomInt(0, 5)]
            # Append the random face to a list of faces
            faceList.append(face)
          
        x = 0
        for col in range(self._cols):
            for row in range(self._rows):
                # For each coordinate in the grid, give it a face value from the list of faces.
                face = faceList[x] 
                x += 1
                self._grid[col][row] = BoggleLetter(self.getBoard(), col, row, face)
                



    def __str__(self):
        """
        Returns a string representation of this BoggleBoard
        """
        board = ''
        for r in range(self._rows):
            for c in range(self._cols):
                boggleLetter = self._grid[c][r]
                color = boggleLetter.getTextColor()
                letter = boggleLetter.getLetter()
                board += '[{}:{}] '.format(letter,color)
            board += '\n'
        return board


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # Uncomment this code when you are ready to test it!
    
    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!
    
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard(win)
    print(board)
    
    keepGoing = True
    while keepGoing:
        pt = win.getMouse()
        if board.inExit(pt):
            keepGoing = False
        elif board.inGrid(pt):
            (col, row) = board.getPosition(pt)
            print("{} at {}".format(board._grid[col][row], (pt.getX(), pt.getY())))
        elif board.inReset(pt):
            board.reset()
