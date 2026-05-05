import random
states = ["patrol","chase","search"]

p = [
    [0.8,0.2,0.0], #patrol
    [0.2,0.6,0.2], #chase
    [0.3,0.3,0.4] #search
]

def nextstate(current):
    probs = p[current]
    total = 0
    r = random.uniform(0,1)
    for i in range(3):
        total += probs[i]
        if r <= total:
            return i
        
def run():
    current = 0 
    chasecount = 0

    for _ in range(20):
        current = nextstate(current)
        if current == 1:
            chasecount += 1

    if chasecount >= 5:
        return 1
    return 0

trials = 100000
success = 0
for _ in range(trials):
    success += run()

print("chances of chasing: ",success/trials)
