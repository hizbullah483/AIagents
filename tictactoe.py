board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def checkwinner(b):
    for row in b:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col] != ' ':
                return b[0][col]
        
        if b[0][0] == b[1][1] == b[2][2] != ' ':
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != ' ':
            return b[0][2]
    return None

def ismovesleft(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                return True
    return False

def evaluate(b):
    winner = checkwinner(b)
    if winner == 'X':
        return 10
    elif winner == 'O':
        return -10
    else:
        return 0


def alphabeta(alpha,beta,ismaxplayer):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    
    if not ismovesleft:
        return 0
    
    if ismaxplayer:
        bestval = -999
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = alphabeta(alpha,beta,False)
                    bestval = max(bestval,value)
                    board[i][j] = ' '
                    alpha = max(alpha,bestval)
                    if alpha >= beta:
                        break
        return bestval
    
    else:
        bestval = 999
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    value = alphabeta(alpha,beta,True)

                    bestval = min(bestval,value)
                    board[i][j] = ' '
                    beta = min(bestval,beta)
                    if alpha >= beta:
                        break
        return bestval


