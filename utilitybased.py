class environment:
    def __init__(self):
        self.area = {
            "rock A": {5,2},
            "rock B": {9,8},
            "rock C": {6,3}
        }

    def percieve(self):
        return self.area
    

class utilitybased:
    def __init__(self):
        self.best_rock = None

    def calculate_utility(self,value,cost):
        return (value * 2) - cost
    
    def act(self,environment):
        rocks = environment.percieve()
        highest_utility = -1

        for rockname, (value,cost) in rocks.items():
            utility = self.calculate_utility(value,cost)
            if(utility > highest_utility):
                highest_utility = utility
                self.best_rock = rockname

        return self.best_rock
    

def runagent(environment,agent):
    best_rock = agent.act(environment)
    print("best rock is ",best_rock)



envir = environment()
agent = utilitybased()
    
runagent(envir,agent)
