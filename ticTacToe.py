Layout of the board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or
        (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
        (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
        (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player) or
        (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or
        (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or
        (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or
        (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player))
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board) #will print the board
        print('Turn for ' + turn + '. Move on which space?') #ask the player which space they want
        move = input() #get the answer the player inputed
        board[move] = turn #places the answer that the player said
        if( checkWinner(board, 'X') ): #check if 'X' won
            print('X wins!') #will print if 'X' won
            break
        elif ( checkWinner(board, 'O') ): #check if 'O' won
            print('O wins!') #will print if 'O' won
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board) #will print the board
    