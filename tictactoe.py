board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def checkwinner(b):
    # rows
    for row in b:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # columns
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != ' ':
            return b[0][col]

    # diagonals
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


def alphabeta(b, alpha, beta, ismaxplayer):

    score = evaluate(b)
    if score == 10 or score == -10:
        return score

    if not ismovesleft(b):
        return 0

    if ismaxplayer:
        bestval = -999

        for i in range(3):
            for j in range(3):

                if b[i][j] == ' ':
                    b[i][j] = 'X'

                    value = alphabeta(b, alpha, beta, False)

                    b[i][j] = ' '

                    bestval = max(bestval, value)
                    alpha = max(alpha, bestval)

                    if beta <= alpha:
                        break
            if beta <= alpha:
                break

        return bestval

    else:
        bestval = 999

        for i in range(3):
            for j in range(3):

                if b[i][j] == ' ':
                    b[i][j] = 'O'

                    value = alphabeta(b, alpha, beta, True)

                    b[i][j] = ' '

                    bestval = min(bestval, value)
                    beta = min(beta, bestval)

                    if beta <= alpha:
                        break
            if beta <= alpha:
                break

        return bestval
