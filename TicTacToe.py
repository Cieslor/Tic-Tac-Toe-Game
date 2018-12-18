


# function that will print out the board
def printBoard():
    for crate in board:
        for item in crate:
            print(item,end = '')
        print()

# game mechanism
player1Check = False
player2Check = False
turn1 = ""
turn2 = ""
turnCounter = 0
checkIfEmpty = True
restartGame = True
import re
check = r'^[1-3] [1-3]$'

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

# start of the game 
print("Welcome to 'Tic Tac Toe Game'")
print("\nInstruction:")
print("To make a turn in game please type in cordinates (for example 1 1 , 2 3 etc).")
while restartGame == True:
    # Creates a new board for single game
    board = [[" "," 1"," 2"," 3"],["1","  ","  ","  "],["2","  ","  ","  "],["3","  ","  ","  "]]
    print("Please enter 'Player 1' name: ",end="")
    player1 = input()
    print("Please enter 'Player 2' name: ",end="")
    player2 = input()
    print()
    print(f"             Lets begin the battle between {player1} and {player2}!!")
    print("The game board:")
    printBoard()

    # Game mechanism loop

    while player1Check == False or player2Check == False :
        # Player1 turn
        while checkIfEmpty: # here we check if the field that player has chosen is empty
            print(f"{player1} turn: ",end ="")
            turn1 = input()
            checking = re.search(check,turn1) # regular expression for checking format of input
            if checking: # here we check if player has chose corectly the field ( for example 1 1 -> right, 11 -> wrong)
                if board[int(turn1.replace(" ","")[0])][int(turn1.replace(" ","")[1])]== " X" or board[int(turn1.replace(" ","")[0])][int(turn1.replace(" ","")[1])] == " O":
                    print("This field is not empty! Chose another one.")
                else:
                    board[int(turn1.replace(" ","")[0])][int(turn1.replace(" ","")[1])]= " X"
                    break
            else:
                print("Wrong format ! Please type cordinates corectly.")
                

        turnCounter+=1
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
        while checkIfEmpty:
            print(f"{player2} turn: ",end ="")
            turn2 = input()
            checking = re.search(check,turn2)
            if checking:
                if (board[int(turn2.replace(" ","")[0])][int(turn2.replace(" ","")[1])] == " X") or (board[int(turn2.replace(" ","")[0])][int(turn2.replace(" ","")[1])] == " O"):
                    print("This field is not empty! Chose another one.")
                else:
                    board[int(turn2.replace(" ","")[0])][int(turn2.replace(" ","")[1])] = " O"
                    break
            else:
                print("Wrong format ! Please type cordinates corectly.")
                
    
        turnCounter+=1
        printBoard()
        # Here we start checking if player2 has won
        if turnCounter >= 5:
            player2Check = winCheck(" O")
        if player2Check == True:
            print(f"{player2} wins!!")
            break

    # asking player if he want to play again
    print("Do you want to play again? (Type in 'yes' or 'no'): ",end ="")
    if  input() == "no":
        print("See you later!!")
        break
   
    
    

    
    
