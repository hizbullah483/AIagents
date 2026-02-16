class environment:
    def __init__(self):
        self.locations = ["blue house","green house","red house","yellow house","white house"]
    def percieve(self,position):
        return self.locations[position]


class goalBased:
    def __init__(self,goal):
        self.goal = goal

    def act(self,percept):
        if (percept == self.goal):
            print("found goal. terminating now")
            return 0
        else:
            print("now at ",percept)
            return 1
        
def runagent(environment,agent):
    flag = 1
    for i in range(len(environment.locations)):
        percept = environment.percieve(i)
        flag = agent.act(percept)
        if (flag == 0):
            break


envir = environment()
agent = goalBased("red house")
runagent(envir,agent)
