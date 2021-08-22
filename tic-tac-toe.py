from colors import printColor
# Print Board
def printTTT(board, color1, color2):
    if len(board) != 9:
        return "Your list must be 9 numbers long"
    
    rowPos = 0
    for i in range(3):
        print(f"{rowPos+1}        |{rowPos+2}        |{rowPos+3}        ")
        print("    ", end="")
        if board[rowPos] == 1:
            print(printColor("x", color1, "return"), end="")
        elif board[rowPos] == 2:
            print(printColor("o", color2, "return"), end="")
        elif board[rowPos] == 0:
            print(" ", end="")
        print("    |", end="")

        print("    ", end="")
        if board[rowPos+1] == 1:
            print(printColor("x", color1, "return"), end="")
        elif board[rowPos+1] == 2:
            print(printColor("o", color2, "return"), end="")
        elif board[rowPos+1] == 0:
            print(" ", end="")
        print("    |", end="")

        print("    ", end="")
        if board[rowPos+2] == 1:
            print(printColor("x", color1, "return"), end="")
        elif board[rowPos+2] == 2:
            print(printColor("o", color2, "return"), end="")
        elif board[rowPos+2] == 0:
            print(" ", end="")
        print("    ")

        print("         |         |        ")
        print(" ---------------------------")
        rowPos+=3
# CHeck Move
def checkmove(board, move):
    moveindex = move-1
    if moveindex < 0 or moveindex > 8:
        return False
    elif board[moveindex] == 0:
        return True
    else:
        return False
# Check Turn
def xoroturn(turn):
    if (turn % 2) != 0:
        return 1
    else:
        return 2
# Check Win
def checkwin(board, turn):
    xwin = None
    owin = None
    if board[2] == 1 and board[4] == 1 and board[6] == 1:
        xwin = True
    elif board[0] == 1 and board[4] == 1 and board[8] == 1:
        xwin = True
    elif board[0] == 1 and board[3] == 1 and board[6] == 1:
        xwin = True
    elif board[1] == 1 and board[4] == 1 and board[7] == 1:
        xwin = True
    elif board[2] == 1 and board[5] == 1 and board[8] == 1:
        xwin = True
    elif board[0] == 1 and board[1] == 1 and board[2] == 1:
        xwin = True
    elif board[3] == 1 and board[4] == 1 and board[5] == 1:
        xwin = True
    elif board[6] == 1 and board[7] == 1 and board[8] == 1:
        xwin = True
    if board[2] == 2 and board[4] == 2 and board[6] == 2:
        owin = True
    elif board[0] == 2 and board[4] == 2 and board[8] == 2:
        owin = True
    elif board[0] == 2 and board[3] == 2 and board[6] == 2:
        owin = True
    elif board[1] == 2 and board[4] == 2 and board[7] == 2:
        owin = True
    elif board[2] == 2 and board[5] == 2 and board[8] == 2:
        owin = True
    elif board[0] == 2 and board[1] == 2 and board[2] == 2:
        owin = True
    elif board[3] == 2 and board[4] == 2 and board[5] == 2:
        owin = True
    elif board[6] == 2 and board[7] == 2 and board[8] == 2:
        owin = True
    
    if xoroturn(turn) == 1:   
        if xwin == True:
            return "xwins"
        else:
            return False
    if xoroturn(turn) == 2:   
        if owin == True:
            return "owins"
        else:
            return False

# Make Move
def makemove(board, pos, turn):
    cBoard = board.copy()
    if checkmove(board, pos):
        move = pos-1
        if xoroturn(turn) == 1:
            cBoard[move] = 1
        else:
            cBoard[move] = 2
        return cBoard
    else:
        print("Not a vaild move")

board = [0,0,0,0,0,0,0,0,0]
turn = 1

def playTTT():
    board = [0,0,0,0,0,0,0,0,0]
    turn = 1
    playing = True
    print("""
    Welcome To The Tic-Tac-Toe Game!
    Grab a friend and begin!
    Inscturctions:
        Enter a number between 1-9 
        The number you input will make a x or o apper in the square that contains your number
    """)
    color1 = input(f"What would play 1/X color like to be? Pick from: \n - {printColor('red', 'red', 'return')}\n - {printColor('green', 'green', 'return')} \n - {printColor('yellow', 'yellow', 'return')} \n - {printColor('blue', 'blue', 'return')} \n - {printColor('voilet', 'voilet', 'return')} \n - {printColor('beige', 'beige', 'return')} \n")
    color2 = input(f"What would play 2/O color like to be? Pick from: \n - {printColor('red', 'red', 'return')}\n - {printColor('green', 'green', 'return')} \n - {printColor('yellow', 'yellow', 'return')} \n - {printColor('blue', 'blue', 'return')} \n - {printColor('voilet', 'voilet', 'return')} \n - {printColor('beige', 'beige', 'return')} \n")
    print(printColor('1', color1, 'return')==None)
    if color1 == color2:
        print("Player 2's color should not be the same as color 1")
        color2 = input(f"What would play 2/O color like to be? Pick from: \n - {printColor('red', 'red', 'return')}\n - {printColor('green', 'green', 'return')} \n - {printColor('yellow', 'yellow', 'return')} \n - {printColor('blue', 'blue', 'return')} \n - {printColor('voilet', 'voilet', 'return')} \n - {printColor('beige', 'beige', 'return')} \n")
        while color2 == color1:
                print("Player 2's color should not be the same as color 1")
                color2 = input(f"What would play 2/O color like to be? Pick from: \n - {printColor('red', 'red', 'return')}\n - {printColor('green', 'green', 'return')} \n - {printColor('yellow', 'yellow', 'return')} \n - {printColor('blue', 'blue', 'return')} \n - {printColor('voilet', 'voilet', 'return')} \n - {printColor('beige', 'beige', 'return')} \n")
    if printColor('1', color1, 'return') == None:
        print("That is not a availibel color player 1. Your color will be blue")
        color1 = 'blue'
    if printColor('2', color2, 'return') == None:
        print("That is not a availibel color player 1. Your color will be beige")
        color2 = 'beige'
        
    # if color1 != 'red' or color1 != 'green' or color1 != 'yellow' or color1 != 'blue' or color1 != 'voilet' or color1 != 'beige':
    #     print("That is not a availibel color player 1. Your color will be blue")
    #     color1 = 'blue'
    # else:
    #     pass
    # if color2 != 'red' or color2 != 'green' or color2 != 'yellow' or color2 != 'blue' or color2 != 'voilet' or color2 != 'beige':
    #     while color2 != 'red' or color2 != 'green' or color2 != 'yellow' or color2 != 'blue' or color2 != 'voilet' or color2 != 'beige':
    #         print("That is not a availibel color player 1")
    #         color2 = input(f"What would play 1/X color like to be? Pick from: \n - {printColor('red', 'red', 'return')}\n - {printColor('green', 'green', 'return')} \n - {printColor('yellow', 'yellow', 'return')} \n - {printColor('blue', 'blue', 'return')} \n - {printColor('voilet', 'voilet', 'return')} \n - {printColor('beige', 'beige', 'return')} \n")

    printTTT(board, color1, color2)
    while playing == True:
        for i in range(10):
            if turn == 10:
                print("It is a draw!")
                playAgain = input("Would you like to play again type y/n or yes/no: ")
                if playAgain.lower() == "y" or playAgain.lower() == "yes":
                    board = [0,0,0,0,0,0,0,0,0]
                    turn = 1
                    playing = True
                elif playAgain.lower() == "n" or playAgain.lower() == "no":
                    playing = False
                    print("Thank you for playing Tic-Tac-Toe! Hope to see you again soon!")

            if xoroturn(turn) == 1:
                print("X's Turn")
                Xmove = input("What is you move?")
                while Xmove == "":
                    printColor("Sorry, you need to enter a number.", "yellow", "print")
                    Xmove = input("What is you move?")
                Xmove = int(Xmove)
                if checkmove(board, Xmove) == False:
                    while checkmove(board, Xmove) == False:
                            printColor(f"Sorry square {Xmove} is already filled. ", "yellow", "print")
                            Xmove = input(f"What is you move?")
                            while Xmove == "":
                                printColor("Sorry, you need to enter a number.", "yellow", "print")
                                Xmove = input("Sorry, you need to enter a number. What is you move?")
                            Xmove = int(Xmove)
                board = makemove(board, Xmove, turn)
                printTTT(board, color1, color2)    
            else:
                print("O's Turn")
                Omove = input("What is you move?")
                while Omove == "":
                    printColor("Sorry, you need to enter a number.", "yellow", "print")
                    Omove = input("What is you move?")
                Omove = int(Omove)
                if checkmove(board, Omove) == False:
                    while checkmove(board, Omove) == False:
                            printColor(f"Sorry square {Omove} is already filled. ", "yellow", "print")
                            Omove = input("What is you move?")
                            while Omove == "":
                                printColor("Sorry, you need to enter a number.", "yellow", "print")
                                Omove = input("What is you move?")
                            Omove = int(Omove)
                board = makemove(board, Omove, turn)
                printTTT(board, color1, color2)
            win = checkwin(board, turn)
            if win == "xwins":
                print("X has won the game!!!")
                break
            elif checkwin(board, turn) == "owins":
                print("O has won the game!!!")
                break
            turn+=1

        playAgain = input("Would you like to play again type y/n or yes/no: ")
        if playAgain.lower() == "y" or playAgain.lower() == "yes":
            board = [0,0,0,0,0,0,0,0,0]
            turn = 1
            playTTT()
        elif playAgain.lower() == "n" or playAgain.lower() == "no":
            playing = False
            printColor("Thank you for playing Tic-Tac-Toe! Hope to see you again soon!", "green", "print")

playTTT()