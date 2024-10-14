import copy

gameStates = {}

def printBoard(board):
    print()
    for row in board:
        print(row[0] + " " + row[1] + " " + row[2])
        print()

def result(board, player):
    for row in board:
        if(row[0] == row[1] and row[1] == row[2] and row[0] != "*"):
            return 2 if row[0] == player else 0
    
    for column in range(0, 3):
        if(board[0][column] == board[1][column] 
           and board[1][column] == board[2][column] 
           and board[0][column] != "*"):
            return 2 if board[0][column] == player else 0
    
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "*"):
        return 2 if board[0][0] == player else 0
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "*"):
        return 2 if board[0][2] == player else 0
    
    full = True

    for row in board:
        for cell in row:
            if cell == "*":
                full = False
                break
    
    if full:
        return 1
    
    return "NIL"

def evaluate(board, player):
    codedBoard = tuple(tuple(subList) for subList in board)
    if gameStates.get(codedBoard, -1) != -1:
        return gameStates[codedBoard]
    results = []
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i][j] == "*"):
                temp = copy.deepcopy(board)
                temp[i][j] = player
                resultant = result(temp, player)
                if resultant == "NIL":
                    moveArray = evaluate(temp, "X" if player == "O" else "O")
                    resultant = None
                    if 2 in moveArray:
                        resultant = 0
                    elif 1 in moveArray:
                        resultant = 1
                    else:
                        resultant = 2
                results.append(resultant)
    gameStates[codedBoard] = results
    return results


board = [["*", "*", "*"], 
         
         ["*", "*", "*"], 

         ["*", "*", "*"]]

userInput = input("Do you want to go first yes/no: ").lower()

bot = "X"
user = "O"

turn = user if userInput == "yes" else bot

while result(board, turn) == "NIL":

    printBoard(board)

    if turn == user:
        ind1 = int(input()) - 1
        ind2 = int(input()) - 1
        ind1 -= 1
        ind2 -= 1
        board[ind1][ind2] = user
    else:
        moveList = evaluate(board, turn)
        bestMove = None
        maxNum = -1
        for i in range(0, len(moveList)):
            if moveList[i] > maxNum:
                bestMove = i + 1
                maxNum = moveList[i]
        count = 0
        for row in range(0, 3):
            for cell in range(0, 3):
                if board[row][cell] == "*":
                    count += 1
                if count == bestMove:
                    board[row][cell] = turn
                    break
            if count == bestMove:
                break
    turn = bot if turn == user else user 

printBoard(board)

if(result(board, user) == 1):
    print("DRAW")
elif result(board, user) == 2:
    print("YOU WIN :(")
else:
    print("I WIN! :)")