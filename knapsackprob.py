import random

weights = [5, 8, 3, 2, 7, 4]
values =  [10, 15, 7, 8, 12, 5]
wlimit = 15

def totalvalue(currentitems):
    val = 0
    weight = 0
    for i in range(len(currentitems)):
        val += currentitems[i] * values[i]
        weight += currentitems[i] * weights[i]
    if weight > wlimit:
        return 0
    return val

def mutation(currentitems):
    if random.uniform(0,1) < 0.1:
        mutateindex = random.randint(0,5)
        currentitems[mutateindex] = 1 if currentitems[mutateindex] == 0 else 0
    return currentitems

def doublesplit(parent1,parent2):
    split1 = random.randint(1,2)
    split2 = random.randint(3,5)

    return parent1[:split1] + parent2[split1:split2] + parent1[split2:]

def initialize():
    currentitems = []
    for i in range(len(weights)):
        currentitems.append(random.randint(0,1))
    return currentitems

def geneticblast(popsize=100,maxgen=100):
    queue = []
    for _ in range(popsize):
        queue.append(initialize())

    for gen in range(maxgen):
        queue.sort(key=lambda x:totalvalue(x), reverse=True)

        nextgen = queue[:popsize // 2]

        while len(nextgen) < popsize:
            parent1 = random.choice(queue[:popsize // 2])
            parent2 = random.choice(queue[:popsize // 2])

            child = doublesplit(parent1,parent2)
            child = mutation(child)
            nextgen.append(child)

        queue = nextgen
    
    bestsol = max(queue,key=lambda x:totalvalue(x))
    bestvalue = totalvalue(bestsol)
    print(bestsol,bestvalue)

geneticblast()

    
        


