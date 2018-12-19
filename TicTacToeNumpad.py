from IPython.display import clear_output
gameBoard = [""," "," "," "," "," "," "," "," "," "]
inctructionBoard = ["",'1','2','3','4','5','6','7','8','9']
# function that will print a board
def printBoard(board):
    clear_output()
    print("   "+board[7]+ "|" + board[8] + "|" + board[9] )
    print("   "+board[4]+ "|" + board[5] + "|" + board[6] )
    print("   "+board[1]+ "|" + board[2] + "|" + board[3] )

# function asking for what symbol player wants to choose
def askForSymbol():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O:')
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

# function checking of player won
def checkIfWon(board,player_marker):
    if board[7] == board[8] == board[9] == player_marker:
        return True
    elif board[4] == board[5] == board[6] == player_marker:
        return True
    elif board[1] == board[2] == board[3] == player_marker:
        return True
    elif board[7] == board[5] == board[3] == player_marker:
        return True
    elif board[7] == board[4] == board[1] == player_marker:
        return True
    elif board[8] == board[5] == board[2] == player_marker:
        return True
    elif board[9] == board[6] == board[3] == player_marker:
        return True
    elif board[1] == board[5] == board[9] == player_marker:
        return True
    else:
        return False

# function that take player input and place it on board
def placeSymbol(player_marker,index):
    gameBoard[index] = player_marker

listOfPlaces = ['1','2','3','4','5','6','7','8','9']
# function for gameplay
def gamePlay(player):
    index = input()
    while index not in listOfPlaces or gameBoard[int(index)] != " ":
        print("Wrong number! Please choose correct one:",end="")
        index = input()
    placeSymbol(player,int(index))
    printBoard(gameBoard)
    if checkIfWon(gameBoard,player) == True:
        return True
    else:
        return False
print("Instruction: use numpad (1-9) to place symbols.")
printBoard(inctructionBoard) 
# function for restarting
def restartGame():
    print("Do you want to play again? (type 'yes' or 'no'): ",end = "")
    restartKey = input()
    while restartKey != 'yes' and restartKey != 'no':
        print("Wrong answer, please choose correct one:",end="")
        restartKey = input() 
    if restartKey == 'yes':
        gameBoard = [""," "," "," "," "," "," "," "," "," "]
        return True
    else:
        return False     
# main gameloop
restart = True
while True:
    player1,player2 = askForSymbol()
    turnCounter = 0
    while True:
        print("Player1 please pick a place:",end="")
        if gamePlay(player1) == True:
            print("Player1 has won!")
            break
        turnCounter+=1
        if turnCounter == 9:
            print("It is a draw!")
            break
        print("Player2 please pick a place:",end="")
        if gamePlay(player2) == True:
            print("Player2 has won!")
            break
        turnCounter+=1
    if restartGame() == False:
        break









    
    
   
    
    