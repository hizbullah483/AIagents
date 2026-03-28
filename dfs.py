graph = {
    "Entrance" : ["hallwayA","hallwayB"],
    "hallwayA" : ["storage"],
    "hallwayB" : ["target"],
    "target" : [],
    "deepvault" : [],
    "storage" : ["deepvault"]
}

limit = 2
stack = [[0,["Entrance"]]]
visited = []

while len(stack) > 0:
    currentdepth,currentpath = stack.pop()
    if currentdepth > limit:
        continue
    currentlocation = currentpath[-1]

    if currentlocation == "target":
        print(currentpath," at depth ",currentdepth)
        break

    if currentlocation not in visited:
        visited.append(currentlocation)
        for neighbour in graph.get(currentlocation):
            newpath = currentpath + [neighbour]
            stack.append((currentdepth+1,newpath))

