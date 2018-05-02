import helpersMax
from random import shuffle

def randomMutation(testLength):
    middleGenome = [i for i in range(1, testLength)]
    shuffle(middleGenome)
    return [0] + middleGenome + [testLength]

bound = 0
current = [0] * 19
best = []
melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
#melanoGenome = [0,11,2,17,8,13,3,14,10,15,5,7,16,1,12,4,6,9,18]
#melanoGenome = randomMutation(15)
mirandaGenome = [i for i in range(len(melanoGenome))]
print(melanoGenome)
# grafiek maken met verschillende lengtes van melanoGenome -> line op fitten met voorspellingen kijken of of klopt
# verschillende breakpoints in de grafiek? -> difficulty? 
# branch and bound combi met beam search -> ipv checken naar oplossing, checken voor 2 of 3 lagen buiten oplossing? 
# bound vanaf 0 en dan omhoog?
def BnB(genome, depth, bound, current, best):
    if genome == mirandaGenome:

        if depth <= bound:
            bound, best = depth, current
            print(bound)
            print(best)
            return bound, current, best
    else:
        breakpoints = helpersMax.FindBreakpointPairs(genome)
        #checken of 0 moves hier lang duren

        for options in helpersMax.Mutate(genome, "B&B"):
            for option in options:
                # voor de bound tellen hoeveel 1 moves er worden gemaakt in de greedy, dit laat de maximum improvement zien
                # als je altijd 1 breakpoint weghaalt is de lower bound / 2 (hierom dus die / 2)
                if int(helpersMax.LowBound(helpersMax.Reverse(genome, option[0], option[1]))) + depth + 1 < bound: 
                    current[depth] = (option[0], option[1])
                    bound, current, best = BnB(helpersMax.Reverse(genome, option[0], option[1]), depth + 1, bound, current, best)
        return bound, current, best
# get the upper bound from Greedy
bound = helpersMax.Greedy(melanoGenome)
print(bound)
BnB(melanoGenome, 0, 13, current, best)
print(melanoGenome)