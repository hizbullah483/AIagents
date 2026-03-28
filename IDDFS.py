def dls(graph,start,goal,limit):
  stack = [[0,[start]]]
  visited = []

  while len(stack) > 0:
      currentdepth,currentpath = stack.pop()
      if currentdepth > limit:
          continue
      currentlocation = currentpath[-1]
      if currentlocation == goal:
          print("goal found at depth ",currentdepth,currentpath)
          return 1

      if currentlocation not in visited:
          visited.append(currentlocation)
          for neighbour in graph.get(currentlocation):
              newpath = currentpath + [neighbour]
              newdepth = currentdepth + 1
              stack.append((newdepth,newpath)) 


def iddfs():
    graph = {
        "mainbox" : ["zoneA","zoneB"],
        "zoneA" : ["switch1","switch2"],
        "zoneB" : ["breaker101"],
        "switch1" : [],
        "switch2" : [],
        "breaker101" : []
    }

    result = 0
    for currentdepth in range(3):
        result = dls(graph,"mainbox","breaker101",currentdepth)
        if result == 1:
            return
        

iddfs()
