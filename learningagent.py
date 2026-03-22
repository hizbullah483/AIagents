import random

alpha = 0.1
gamma = 0.9
epsilon = 0.2

actions = ["cheese","trap","nothing"]
rewards = {"cheese": 10,"trap": -10,"nothing": -1}
qtable = {"cheese": 0.0,"trap": 0.0,"nothing": 0.0}

for episode in range(1,51):
    if random.uniform(0,1) < epsilon:
        chosenaction = random.choice(actions)
    else:
        chosenaction = max(qtable, key=qtable.get) ################################################

    reward = rewards[chosenaction]
    oldmemory = qtable[chosenaction]

    newmemory = oldmemory + ((reward * alpha * gamma) - (oldmemory))
    qtable[chosenaction] = newmemory
    print(qtable)
