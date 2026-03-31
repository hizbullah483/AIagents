graph = {
    'S' : {'A' : 2,'B' : 5, 'C':4},
    'A' : {'D':7,'E':3},
    'B' : {'F':6},
    'C' : {'G':2},
    'D' : {'T':4},
    'E' : {'T':6},
    'F' : {'T':5},
    'G' : {'T':3},
    'T' : {}
}

def bidenblast(graph,start,goal,width):
    queue = [[0,[start]]]

    while len(queue) > 0:
        candidates = []

        for currentg,currentpath in queue:
            currentlocation = currentpath[-1]
            if currentlocation == goal:
                print(currentg,currentpath)
                return
            
            for neighbour,pathcost in graph.get(currentlocation).items():
                if neighbour not in currentpath:
                    newpath = currentpath + [neighbour]
                    newg = currentg + pathcost
                    candidates.append((newg,newpath))

            candidates.sort(key=lambda x:x[0])
            queue = candidates[:width]

bidenblast(graph,'S','T',2)
