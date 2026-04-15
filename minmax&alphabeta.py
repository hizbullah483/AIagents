tree = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G','H'],
    'D' : ['I','J','K'],
    'E' : ['L','M'],
    'F' : ['N','O'],
    'G' : ['P','Q'],
    'H' : ['R'],
    'I' : [],
    'J' : [],
    'K' : [],
    'L' : [],
    'M' : [],
    'N' : [],
    'O' : [],
    'P' : [],
    'Q' : [],
    'R' : []
}

scores = {
    'I': 5,
    'J': 7,
    'K': 1,
    'L': 9,
    'M': 2,
    'N': 5,
    'O': 10,
    'P': 12,
    'Q': 6,
    'R': 20
}

def minmax(node,depth,ismaxplayer):
    if len(tree[node]) == 0:
        return scores[node]
    
    if ismaxplayer:
        bestval = -999
        for child in tree[node]:
            value = minmax(child,depth + 1, False)
            bestval = max(bestval,value)
        return bestval
    
    else:
        bestval = 999
        for child in tree[node]:
            value = minmax(child,depth + 1, True)
            bestval = min(value,bestval)
        return bestval
    


winner = minmax('A',0,False)
print("winner is ",winner)

def alphabeta(node,depth,alpha,beta,ismaxplayer):
    if len(tree[node]) == 0:
        return scores[node]
    
    if ismaxplayer:
        bestval = float('-inf')
        for child in tree[node]:
            value = alphabeta(child,depth + 1,alpha,beta,False)
            bestval = max(bestval,value)

            alpha = max(alpha,bestval)
            if beta <= alpha:
                break
        return bestval
    
    else:
        bestval = float('inf')
        for child in tree[node]:
            value = alphabeta(child,depth + 1,alpha,beta,True)
            bestval = min(bestval,value)

            beta = min(beta,bestval)
            if beta <= alpha:
                break
        return bestval


winner = alphabeta('A',0,-999,999,False)


print("winner is ",winner)



