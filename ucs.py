graph = {
        'Earth': {'Moon_Base': 10, 'Orbital_Platform': 5},
        'Orbital_Platform': {'Moon_Base': 2, 'Mars': 60},
        'Moon_Base': {'Mars': 50},
        'Mars': {} # Goal location
    }

#each list in queue has a cost and a path list
queue = [[0,["Earth"]]]
visited = []

while len(queue) > 0:
    queue.sort(key=lambda x: x[0]) #x tells one list. x[0] tells first element of list

    currentcost, currentpath = queue.pop(0)
    currentlocation = currentpath[-1]
    if currentlocation == "Mars":
        print("cost: ",currentcost," path: ",currentpath)
        break

    if currentlocation not in visited:
        visited.append(currentlocation)

        for neighbour, stepcost in graph.get(currentlocation).items():
            newpath = currentpath + [neighbour]
            newcost = currentcost + stepcost

            queue.append((newcost,newpath))

