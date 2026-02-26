graph = {
    'Tehran': ['Baghdad', 'Istanbul'],
        'Baghdad': ['Cairo'],
        'Istanbul': ['Berlin'],
        'Cairo': ['Washington'],
        'Berlin': ['Washington'],
        'Washington': []
}

queue = [["Tehran"]]
visited = []

while len(queue) > 0:
    currentpath = queue.pop(0)
    currentlocation = currentpath[-1]
    if currentlocation == "Washington":
        print(currentpath)
        break
    
    if currentlocation not in visited:
        visited.append(currentlocation)

        for neighbour in graph.get(currentlocation):
            newpath = currentpath + [neighbour]
            queue.append(newpath)
