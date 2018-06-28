height = 6
width = 7
board = [[] for i in range(width)]

def printBoard():
    for i in range(width):
        print (" " + str(i), end="")
    print()
    for i in range(height-1,-1,-1):
        for j in range(width):
            if len(board[j]) > i:
                print ("|" + str(board[j][i]), end="")
            else:
                print ("| ", end="")
        print("|")

def inProgress():
    for i in range(width):
        for j in range(len(board[i])-3):
            if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2] and board[i][j] == board[i][j+3]:
                return False
    for i in range(height):
        for j in range(width-3):
            if i < len(board[j]) and i < len(board[j+1]) and i < len(board[j+2]) and i < len(board[j+3]) and board[j][i] == board[j+1][i] and board[j][i] == board[j+2][i] and board[j][i] == board[j+3][i]:
                return False
    return True

printBoard()
player = 1

while inProgress():
    move = int(input("Player " + str(player) + " choose your column: "))
    if len(board[move]) < height:
        board[move].append(player)
        printBoard()
        player = 3 - player
    else:
        print ("That column is full!")

print ("Game over! Player", 3-player, "wins!")
