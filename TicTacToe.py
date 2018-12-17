# project of the board
board = [[" "," 1"," 2"," 3"],["1","  ","  ","  "],["2","  ","  ","  "],["3","  ","  ","  "]]

# function that will print out the board
def printBoard():
    for crate in board:
        for item in crate:
            print(item,end = '')
        print()

# start of the game 
print("Welcome to 'Tic Tac Toe Game'")

print("Please enter 'Player 1' name: ",end="")
player1 = input()

print("Please enter 'Player 2' name: ",end="")
player2 = input()
print()

print(f"             Lets begin the battle between {player1} and {player2}!!")
print("\nInstruction:")
print("To make a turn in game please type in cordinates (for example 1 1 , 2 3 etc).")
print("The game board:")
printBoard()

# game mechanism
player1Check = False
player2Check = False
turn1 = ""
turn2 = ""
turnCounter = 0

# function that will check if player won
def winCheck(string):
    if (board[1][1] == string and board[1][2] == string and board[1][3] == string):
        return True
    elif (board[2][1] == string and board[2][2] == string and board[2][3] == string):
        return True
    elif (board[3][1] == string and board[3][2] == string and board[3][3] == string):
        return True
    elif (board[1][1] == string and board[2][2] == string and board[3][3] == string):
        return True
    elif (board[1][3] == string and board[2][2] == string and board[3][1] == string):
        return True
    elif (board[1][1] == string and board[2][1] == string and board[3][1] == string):
        return True
    elif (board[1][2] == string and board[2][2] == string and board[3][2] == string):
        return True
    elif (board[1][3] == string and board[2][3] == string and board[3][3] == string):
        return True
    else:
        return False
    



# main loop for game

while player1Check == False or player2Check == False :
    # Player1 turn
    print(f"{player1} turn: ",end ="")
    turn1 = input()
    turnCounter+=1
    board[int(turn1.replace(" ","")[0])][int(turn1.replace(" ","")[1])]= " X"
    printBoard()
    # Here we start checking if player1 has won
    if turnCounter >= 5:
        player1Check = winCheck(" X")
    if player1Check == True:
        print(f"{player1} wins!!")
        break
    # Player1 has last turn at turnCounter == 9
    # So we call a draw if noone has wone before
    if turnCounter == 9:
        print("Draw!!")
        break
    # Player2 turn
    print(f"{player2} turn:",end ="")
    turn2 = input()
    turnCounter+=1
    board[int(turn2.replace(" ","")[0])][int(turn2.replace(" ","")[1])]= " O"
    printBoard()
    # Here we start checking if player2 has won
    if turnCounter >= 5:
        player2Check = winCheck(" O")
    if player2Check == True:
        print(f"{player2} wins!!")
        break
   
    
    

    
    
