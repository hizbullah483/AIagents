import random
#survive breed mutate die


matrix = [
    [4, 6, 8, 7, 5],
    [7, 5, 6, 8, 4],
    [6, 4, 7, 5, 8],
    [5, 8, 6, 4, 7],
    [8, 6, 5, 7, 4],
    [7, 4, 8, 6, 5],
    [6, 7, 4, 5, 8],
    [5, 6, 7, 8, 4],
    [4, 7, 5, 6, 8],
    [8, 5, 6, 4, 7]
]

def getcost(currentpath):
    cost = 0
    for taskindex in range(10):
        machineindex = currentpath[taskindex]
        cost += matrix[taskindex][machineindex]
    return cost

def geneticblast(matrix,width,maxgen=100):
    queue = []

    for _ in range(width):
        randompath = [random.randint(0,4) for _ in range(10)]
        randomg = getcost(randompath)
        queue.append((randomg,randompath))

    generation = 0
    while len(queue) > 0 and generation <= maxgen:
        candidates = []
        queue.sort(key=lambda x:x[0])

        survivors = queue[:width // 2]
        for survivorg, survivorpath in survivors:
            candidates.append((survivorg,survivorpath))

        while len(candidates) < width:
            parent1 = random.choice(survivors)[1]
            parent2 = random.choice(survivors)[1]

            split = random.randint(1,8)
            newpath = parent1[:split] + parent2[split:]

            if random.uniform(0,1) < 0.1:
                mutateindex = random.randint(0,9)
                newpath[mutateindex] = random.randint(0,4)

            newg = getcost(newpath)
            candidates.append((newg,newpath))

        candidates.sort(key=lambda x:x[0])
        queue = candidates[:width]
        generation += 1

    bestg,bestpath = queue.pop(0)
    print(bestg,bestpath)


geneticblast(matrix, width=10)
geneticblast(matrix, width=30)
geneticblast(matrix, width=100)






