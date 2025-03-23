# Let's Play Boggle!

## 📖 Overview

**Let's Play Boggle** is a digital version of the classic Boggle word search game, where the objective is to form words by linking together adjacent letters from a 4x4 grid of dice. 

Our implementation adapts the traditional Boggle format into a single-player version with a graphical user interface (GUI) using the `graphics.py` library.

## 🕹️ Features

- **Randomly Generated Grid**: The grid of letters is randomized each time a new game is started.
- **Word Formation**: Players can form words by clicking adjacent letters in the grid.
- **Word List**: Displays a list of all valid words found during the game.
- **Reset and Exit Options**: Players can reset the game or exit at any time.
- **Color Feedback**: Letters are highlighted in different colors as words are formed.

## 🎮 Gameplay

In **Boggle**, players form words by connecting adjacent letters in a 4x4 grid. Here's a breakdown of the gameplay mechanics:

### 📚 Creating a Word
- Click on the letters of the grid to form words. Adjacent letters (horizontally, vertically, or diagonally) can be used.
- The currently selected letters are displayed below the grid. As you form a word, the letters will change color to show which ones are part of the word.
- The most recent letter is shown in **blue**, and previously selected letters are displayed in **green**.

### 📝 Completing a Word
- Once a word is fully formed, click on the last letter to confirm the word.
- The word must be at least 3 letters long, not previously entered, and found in the provided dictionary.

### 🔄 Resetting a Word
- If you make a mistake while forming a word, click any non-adjacent letter to reset the word, clearing all selected letters.

### 🚪 Resetting the Game
- Clicking the **RESET** button will shuffle the dice and start a new game, clearing all words and resetting the timer.

### 🎲 Shaking the Dice
- The grid of letters is randomized at the start of the game or after pressing **RESET**. This process uses a randomization algorithm to ensure a fresh board every time.

## Getting Started

### 🛠️ Prerequisites

Before running the game, make sure you have the following:

- **Python 3.x** installed.
- **graphics.py**: A simple graphics library.

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/lesleyiazzag/Let-s-Play-Boggle.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Let's-Play-Boggle
    ```

3. Ensure you have the necessary Python dependencies. You’ll need to have the `graphics.py` file in the same directory.

4. Run the game by executing:

    ```bash
    python bogglegame.py
    ```

### How to Play

1. A 4x4 grid of letters will appear on the screen.
2. Click on adjacent letters to form words. The word will be displayed below the grid.
3. To complete the word, click on the last letter.
4. If you make a mistake, click a non-adjacent letter to reset the current word.
5. To reset the game, click the **RESET** button. To exit, click the **EXIT** button.


## License

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Acknowledgments

- Thanks to the CS134 course at Williams College for the starter code.
- The `graphics.py` library used for GUI elements was developed by John Zelle.

