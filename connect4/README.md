Connect Four Tutorial
======

# Description

Connect four is a game where you have a grid and you must drop your tokens. A sample output could look like this:

```text
Welcome to Cody's Connect Four game.

 0 1 2 3 4 5
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
Player one, select a column: 2

 0 1 2 3 4 5
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | |1| | | |
Player two, select a column: 1

 0 1 2 3 4 5
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| |2|1| | | |
```

This game should play until one of the players has four tokens in a row.

# Implementation

The very first thing we will need are the dimensions of the board, namely ``height`` and ``width``. We will begin with the board being empty, so it should look like this:

```python
height = 6
width = 7
board = [[] for i in range(width)]
```

We will use the following code to print out the board:

```python
def printBoard():
    for i in range(width):
        print (" " + str(i), end="")
    print()
    for i in range(height-1,-1,-1):
      for j in range(width):
        if (len(board[j])) > i:
          print ("|" + board[j][i], end="")
        else:
          print("| ", end="")
        print("|")
```
