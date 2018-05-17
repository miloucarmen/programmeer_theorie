import helpersSteven_MAIL as helpersSteven
import copy
from random import shuffle

def randomMutation(testLength):
    middleGenome = [i for i in range(1, testLength)]
    shuffle(middleGenome)
    return [0] + middleGenome + [testLength]

current = [0] * 32
best = []
#melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
melanoGenome = randomMutation(5)

genomeObject = helpersSteven.GenomeSequence(melanoGenome)
mirandaGenome = [i for i in range(len(melanoGenome))]
def BnB(genomeObj, depth, upperBound, current, best, currentPoints):
    if genomeObj.genome == mirandaGenome:
        if currentPoints <= upperBound:
            best = []
            upperBound, best = currentPoints, current
            best = copy.copy(best)
            return upperBound, current, best


    else:
        allOptions = genomeObj.Mutate("B&B")

        prevPoints = 0
        for optionList in range(len(allOptions)):

            lowerBound = 

            for option in allOptions[optionList]:

                # check if lowerBound is less OR equal than upperBound.
                # (we use leq, because the challenge is: if there are MULTIPLE best solutions, compare them)
                if lowerBound <= upperBound:
                    i, j = option[0], option[1]
                    current[depth] = (i, j)


                    genomeObj.genome = genomeObj.Reverse(i, j)
                    genomeObj.UpdateBreakpointList(i, j)
                    upperBound, current, best = BnB(genomeObj, depth + 1, upperBound, current, best, currentPoints)
                    genomeObj.genome = genomeObj.Reverse(i,j)
                    genomeObj.UpdateBreakpointList(i, j)
                else:
                    break
        return upperBound, current, best

upperBound, current, best = BnB(genomeObject, 0, 9999, current, best, 0)

best = best[:upperBound]
print("Final best: ",best)
print("Melano: ", melanoGenome)

genom = helpersSteven.GenomeSequence(melanoGenome)
for mutations in best:
    genom.genome = genom.Reverse(mutations[0], mutations[1])
print(genom.genome)
