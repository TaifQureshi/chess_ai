import copy

def Reverse(lst): 
    return [ele for ele in reversed(lst)] 



pawnEvalWhite =[[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
                [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
                [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
                [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
                [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
                [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
                [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]

pawnEvalblack = Reverse(pawnEvalWhite)

    # do not reverse

knightEval =[[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
                [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
                [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
                [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
                [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
                [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]


bishopEvalWhite = [[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
                    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
                    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
                    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
                    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
                    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]

bishopEvalblack = Reverse(bishopEvalWhite)

rookEvalWhite = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

rookEvalblack = Reverse(rookEvalWhite)

#do no revrese
evalQueen = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

kingEvalWhite = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

kingEvalblack = Reverse(kingEvalWhite)



def all_moves(board):
    all_mov = []
    for i in range(8):
        for j in range(8):
            if board.board[i][j] != 0:
                if board.board[i][j].color == board.turn:
                    for k in board.board[i][j].update_move(board):
                        all_mov.append([(i,j),k])
    return all_mov

def eval(board):
    value = 0
    for i in range(8):
        for j in  range(8):
            if board.board[i][j] != 0:
                value = value + picevalue(board,i,j)
    check,k = board.is_check()
    
    if check:
        if board.board[k[0]][k[1]].color == 'w':
           value += 2000
        else:
            value -= 2000
    
    return value

def picevalue(board,i,j):
    absval = 0
    if board.board[i][j].get_type() == 'p':
        if board.board[i][j].color == 'w':
            absval = 10 + pawnEvalWhite[i][j]
        else:
            absval = 10 + pawnEvalblack[i][j]
    
    elif board.board[i][j].get_type() == 'r':
        if board.board[i][j].color == 'w':
            absval = 50 + rookEvalWhite[i][j]
        else:
            
            absval = 50 + rookEvalblack[i][j]
    
    elif board.board[i][j].get_type() == 'n':
        absval = 30 + knightEval[i][j]
    
    elif board.board[i][j].get_type() == 'b':
        if board.board[i][j].color == 'w':
            absval = 30 + bishopEvalWhite[i][j]
        else:
            
            absval = 30 + bishopEvalblack[i][j]
    
    elif board.board[i][j].get_type() == 'q':
        absval = 90 + evalQueen[i][j]
        
    elif board.board[i][j].get_type() == 'k':
        if board.board[i][j].color == 'w':
            absval = 900 + kingEvalWhite[i][j]
        else:
            
            absval = 900 + kingEvalblack[i][j]
    if board.board[i][j].color == board.turn:
        return absval
    else:
        return -absval

def minmax(depth,board,alpha,beta,max):
    if depth == 0:
        return eval(board)

    move = all_moves(board)
    if max:
        value = -99999
        for i in move:
            # print(i[0])
            newboard = copy.deepcopy(board)
            piece = newboard.board[i[0][0]][i[0][1]]
            newboard.make_move(i[1],piece)
            value = max(value,minmax(depth-1,newboard,alpha,beta,not max))
            alpha = max(value,alpha)
            if beta <= alpha:
                return value
        
        return value

    else:               
        value = 99999
        for i in move:
            newboard = copy.deepcopy(board)
            piece = newboard.board[i[0][0]][i[0][1]]
            newboard.make_move(i[1],piece)
            value = min(value,minmax(depth-1,newboard,alpha,beta,max))
            beta = min(value,beta)
            if beta <= alpha:
                return value
        
        return value
    

def minmaxroot(depth,board,max):
    move = all_moves(board)
    best = -99999
    bestmove = 0
    for i in move:
        newboard = copy.deepcopy(board)
        piece = newboard.board[i[0][0]][i[0][1]]
        newboard.make_move(i[1],piece)
        value = minmax(depth-1,newboard,-10000,10000,not max)
        if value > best:
            best = value
            bestmove = i

    return bestmove
