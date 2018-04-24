bound = 0 
current = [0] * 19
best = []
melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

bound, best = greedy(melanoGenome)
bAndB(melanoGenome, 0)

def bAndB(genoom, depth, bound):
    if genoom == mirandaGenome:
        if depth < bound:
            bound, best = depth, current
    else:
        for options in mutateOptions(genoom):
            for option in options:
                if int(greedy(reverse(genoom, option[0], option[1])) / 2) + depth + 1 < bound:
                    current[depth + 1] = (option[0], option[1])
                    bAndB(reverse(genoom, option[0], option[1]), depth + 1, bound)
    return bound, best
    
