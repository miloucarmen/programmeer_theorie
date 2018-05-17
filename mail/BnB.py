import helpersSteven_MAIL as helpersSteven
import copy
from random import shuffle

def randomMutation(testLength):
    middleGenome = [i for i in range(1, testLength)]
    shuffle(middleGenome)
    return [0] + middleGenome + [testLength]

current = [0] * 32
best = []
melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
#melanoGenome = randomMutation(20)

genomeObject = helpersSteven.GenomeSequence(melanoGenome)
mirandaGenome = [i for i in range(len(melanoGenome))]

# grafiek maken met verschillende lengtes van melanoGenome -> line op fitten met voorspellingen kijken of of klopt
# verschillende breakpoints in de grafiek? -> difficulty?
# branch and upperBound combi met beam search -> ipv checken naar oplossing, checken voor 2 of 3 lagen buiten oplossing?
# beam search met voorafbepaalde state space
# upperBound vanaf 0 en dan omhoog?


def BnB(genomeObj, depth, upperBound, current, best, breakpointPairs):

    depth0count = 0

    #print("----------Branch and Bound was started-----------")

    #print("Depth: ", depth)
    #print("upperBound: ", upperBound)
    #print("Current: ", current)
    #print("Best: ", best)

    #print("Our current genome looks like this: ", genomeObj.genome)
    if genomeObj.genome == mirandaGenome:

        #print("--------------------------------------!The genome has been SOLVED!--------------------------------------")

        if depth <= upperBound:

            #print("!!A new best has been found!!")

            best = []
            upperBound, best = depth, current
            #print("Updated upperBound: ", upperBound)
            #print("Updated best: ", best)

            #print("Return: upperbound, current, best")

            # print("Depth: ", depth)
            print("upperBound: ", upperBound)
            # print("Current: ", current)
            #print("Best: ", best)

            best = copy.copy(best)
            return upperBound, current, best


    else:
        #print("The genome has not been solved yet.")

        allOptions = genomeObj.Mutate("B&B")
        prevPoints = 0
        #print("The optionList equals: ", allOptions)

        for optionList in range(len(allOptions)):
            breakpointPairsCurrent = breakpointPairs - abs(optionList - 2)

            lowerBound = helpersSteven.LowerBound(breakpointPairsCurrent) + depth

            for option in allOptions[optionList]:

                if depth == 0:
                    depth0count += 1
                    print("Depth = 0: ", depth0count, "out of ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 1:
                    print("-Depth = 1, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 2:
                    print("--Depth = 2, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 3:
                    print("---Depth = 3, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 4:
                    print("----Depth = 4, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 5:
                    print("-----Depth = 5, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 6:
                    print("------Depth = 6, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 7:
                    print("-------Depth = 7, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                if depth == 8:
                    print("--------Depth = 8, # of options here are: ", len(allOptions[0]) + len(allOptions[1]))
                #print("Currently revising from optionList ", optionList, ", ", option)

                # check if lowerBound is less OR equal than upperBound.
                # (we use leq, because the challenge is: if there are MULTIPLE best solutions, compare them)
                if lowerBound <= upperBound:
                    i, j = option[0], option[1]
                    #print("i equals: ", i)
                    #print("j equals: ", j)

                    current[depth] = (i, j)

                    #print("After editing current[depth], current now equals: ", current)

                    genomeObj.genome = genomeObj.Reverse(i, j)

                    #print("After reversing the genome now equals: ", genomeObj.genome)

                    genomeObj.UpdateBreakpointList(i, j)
                    #print("Our breakpointlist is updated and equals: ", genomeObj.breakpointList)

                    #print("We go deeeeeeeepeeeer")
                    upperBound, current, best = BnB(genomeObj, depth + 1, upperBound, current, best, breakpointPairsCurrent)
                    #print("We're out of depth")

                    genomeObj.genome = genomeObj.Reverse(i,j)
                    genomeObj.UpdateBreakpointList(i, j)
                    #print("Our current genome is: einde ", genomeObj.genome)
                    #print("Depth: ", depth)
                    #print("upperBound: ", upperBound)
                    #print("Current: ", current)
                    #print("Best: ", best)
    return upperBound, current, best

breakpointPairs = genomeObject.breakpointPairs
upperBound, current, best = BnB(genomeObject, 0, 13, current, best, breakpointPairs)

best = best[:upperBound]
#print("Final best: ",best)
#print("Melano: ", melanoGenome)

genom = helpersSteven.GenomeSequence(melanoGenome)
for mutations in best:
    genom.genome = genom.Reverse(mutations[0], mutations[1])
#print(genom.genome)
