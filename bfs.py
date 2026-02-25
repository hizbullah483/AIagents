graph = {
    "Tehran" : ["Baghdad","Istanbul"],
    "Baghdad" : ["Cairo"],
    "Istanbul" : ["Berlin"],
    "Berlin" : ["Washington"],
    "Cairo" : ["Washington"],
    "Washington" : []
}

start = "Tehran"
goal = "Washington"

queue = []
visited = []
parent = {}

queue.append(start)
visited.append(start)
parent[start] = None

while len(queue) > 0:
    current = queue.pop(0)
    if current == goal:
        break

    neighbours = graph[current]

    for city in neighbours:

        if city not in visited:
            queue.append(city)
            visited.append(city)
            parent[city] = current

path = []
current = goal
while current != None:
    path.append(current)
    current = parent[current]
path.reverse()
print(path)
