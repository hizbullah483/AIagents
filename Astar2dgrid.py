graph = [
    [1, 1, 1, 5],
    [0, 0, 1, 5],
    [1, 1, 1, 1],
    [1, 0, 0, 1]
]

def getmanhattan(currentlocation,goal):
    return abs(currentlocation[0] - goal[0]) + abs(currentlocation[1] - goal[1])

def getneighbours(currentlocation,graph):
    neighbours = []
    row, col = currentlocation
    rows,cols = len(graph), len(graph[0])
    directions = [(0,-1),(-1,0),(0,1),(1,0)]

    for i,j in directions:
        newrow = i + row
        newcol = j + col
        if 0 <= newrow < rows and 0 <= newcol < cols and graph[newrow][newcol] != 0:
            neighbour = (newrow,newcol)
            pathcost = graph[newrow][newcol]
            neighbours.append((pathcost,neighbour)) 

    return neighbours

def Astar(graph,start,goal):
    startf = getmanhattan(start,goal)
    queue = [[startf,0,[start]]]
    visited = []

    while len(queue) > 0:
        queue.sort(key=lambda x:x[0])
        currentf,currentg,currentpath = queue.pop(0)
        currentlocation = currentpath[-1]

        if currentlocation == goal:
            print(currentpath,currentg)
            return
        
        if currentlocation not in visited:
            visited.append(currentlocation)
            neighbours = getneighbours(currentlocation,graph)
            for pathcost, neighbour in neighbours:
                if neighbour not in visited:
                    newg = currentg + pathcost
                    newf = newg + getmanhattan(neighbour,goal)
                    newpath = currentpath + [neighbour]
                    queue.append((newf,newg,newpath))

Astar(graph,(0,0),(3,3))
