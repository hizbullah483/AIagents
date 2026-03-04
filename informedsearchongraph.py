graph = {
    'S' : {'A' : 3, 'B' : 2},
    'A' : {'C' : 4, 'D' : 1},
    'B' : {'E' : 3, 'F' : 1},
    'C' : {},
    'D':{},
    'E' : {'H' : 5},
    'F' : {'I' : 2,'G' : 3},
    'H':{},
    'I':{},
    'G':{}
}

heuristics = {"A" : 12,"B" : 4,"C" : 7,"D" :3,"E" : 8,"F" : 2,"H" : 4,"I" : 9,"S" : 13,"G" : 0}

def greedyfirst(graph,start,goal):
    queue = [[heuristics[start],[start]]]
    visited = []

    while len(queue) > 0:
        queue.sort(key=lambda x:x[0])
        currenth,currentpath = queue.pop(0)
        currentlocation = currentpath[-1]
        if currentlocation == goal:
            print(currentpath)
            return
        
        if currentlocation not in visited:
            visited.append(currentlocation)
            for neighbour in graph.get(currentlocation):
                if neighbour not in visited:
                    newpath = currentpath + [neighbour]
                    newh = heuristics[neighbour]
                    queue.append((newh,newpath))


greedyfirst(graph,'S','G')

def Astar(graph,start,goal):
    # currentf, current path cost, path
    queue = [[heuristics[start],0,[start]]]
    visited = []
    while len(queue) > 0:
        queue.sort(key=lambda x:x[0])
        currentf, currentg, currentpath = queue.pop(0)
        currentlocation = currentpath[-1]
        
        if currentlocation == goal:
            print(currentpath, currentg)
            return


        if currentlocation not in visited:
            visited.append(currentlocation)

            for neighbour,pathcost in graph.get(currentlocation).items():
                if neighbour not in visited:
                    newpath = currentpath + [neighbour]
                    newg = currentg + pathcost
                    newf = heuristics[neighbour] + newg
                    queue.append((newf,newg,newpath))




Astar(graph,'S','G')
