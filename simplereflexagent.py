class environment:
    def __init__(self):
        self.beds = ["Moist", "Dry", "Moist", "Moist", "Dry", "Moist", "Dry", "Moist", "Moist"]

    def percieve(self,position):
        return self.beds[position]
        
    def act(self,position,action):
        if action == "Water":
            self.beds[position] = "Moist"


class simplereflex:
    def __init__(self):
        pass

    def act(self,percept):
        if percept == "Dry":
            return "Water"
        else:
            return "Move"
        

def runagent(environment,agent):
    print("before: ")
    for i in range(len(environment.beds)):
        print("bed ",i+1," : ",environment.beds[i])

    for i in range(len(environment.beds)):
        percept = environment.percieve(i)
        action = agent.act(percept)
        if(action == "Water"):
            environment.act(i,action)

    print("after")
    for i in range(len(environment.beds)):
        print("bed ",i+1," : ",environment.beds[i])



envir = environment()
agent = simplereflex()
runagent(envir,agent)
