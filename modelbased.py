class environment:
    def __init__(self):
        self.rooms = ['A','C','D','B','D']
    
    def percieve(self,position):
        return self.rooms[position]
    #note how no act in environment s it is unchanged

class modelbased:
    def __init__(self):
        self.haskey = False

    def act(self,percept):
        if(percept == 'D' and self.haskey == True):
            print("D opened")
        elif(percept == 'D'):
            print("Dnot opened as no keycard")
        elif(percept == 'B'):
            self.haskey = True
            print("keycard picked now you can open B")

def runagent(environment,agent):
    for i in range(len(environment.rooms)):
        percept = environment.percieve(i)
        agent.act(percept)


agent = modelbased()
envir = environment()
runagent(envir,agent)
