import helpersSteven_MAIL as helpersSteven
from random import shuffle

def randomMutation(testLength):
    middleGenome = [i for i in range(1, testLength)]
    shuffle(middleGenome)
    return [0] + middleGenome + [testLength]

current = [0] * 10
best = []
#melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
melanoGenome = randomMutation(9)

genomeObject = helpersSteven.GenomeSequence(melanoGenome)
mirandaGenome = [i for i in range(len(melanoGenome))]

# grafiek maken met verschillende lengtes van melanoGenome -> line op fitten met voorspellingen kijken of of klopt
# verschillende breakpoints in de grafiek? -> difficulty?
# branch and upperBound combi met beam search -> ipv checken naar oplossing, checken voor 2 of 3 lagen buiten oplossing?
# beam search met voorafbepaalde state space
# upperBound vanaf 0 en dan omhoog?

def BnB(genomeObj, depth, upperBound, current, best):
##print("Branch and Bound was started!")

    #print("Depth: ", depth)
    #print("upperBound: ", upperBound)
    #print("Current: ", current)
    #print("Best: ", best)

    #print("Our current genome looks like this: ", genomeObj.genome)
    if genomeObj.genome == mirandaGenome:

        #print("----------------------------!The genome has been SOLVED!----------------------------")
        #print("Depth: ", depth)
        #print("upperBound: ", upperBound)
        #print("Current: ", current)
        #print("Best: ", best)

        if depth <= upperBound:
            best = []
            upperBound, best = depth, current
            print("Depth: ", depth)
            print("upperBound: ", upperBound)
            print("Current: ", current)
            print("Best: ", best)

            return upperBound, current, best


    else:
        #print("optionList: ", genomeObj.Mutate("B&B"))
        print("breakpoint pairs", genomeObj.breakpointPairs)
        print("genome", genomeObj.genome)
        allOptions = genomeObj.Mutate("B&B")
        print(allOptions)
        prevPoints = 0
        for optionList in range(len(allOptions)):
            genomeObj.breakpointPairs = genomeObj.breakpointPairs - abs(optionList - 2) + prevPoints
            prevPoints = abs(optionList - 2)
            for option in allOptions[optionList]:
                #print("option: ", option)

                lowerBound = genomeObj.LowerBound() + depth 
                #print("lowerBound is set to: ", lowerBound)
                #print("upperBound was already equal to: ", upperBound)

                # check if lowerBound is less OR equal than upperBound.
                # (we use leq, because the challenge is: if there are MULTIPLE best solutions, compare them)
                if lowerBound <= upperBound:
                    i, j = option[0], option[1]
                    #print("i equals: ", i)
                    #print("j equals: ", j)

                    #print("Depth: ", depth)
                    #print("upperBound: ", upperBound)
                    #print("Current: ", current)
                    #print("Best: ", best)
                    current[depth] = (i, j)

                    #print("After editing current[depth], current now equals: ", current)

                    genomeObj.genome = genomeObj.Reverse(i, j)

                    #print("After reversing the genome now equals: ", genomeObj.genome)

                    genomeObj.UpdateBreakpointList(i, j)

                    #print("Our breakpointlist is updated and equals: ", genomeObj.breakpointList)

                    upperBound, current, best = BnB(genomeObj, depth + 1, upperBound, current, best)

                    genomeObj.genome = genomeObj.Reverse(i,j)
                    genomeObj.UpdateBreakpointList(i, j)
                    genomeObj.breakpointPairs = genomeObj.breakpointPairs + abs(2 - optionList)

                    #print("Our current genome is: einde ", genomeObj.genome)
                    #print("Depth: ", depth)
                    #print("upperBound: ", upperBound)
                    #print("Current: ", current)
                    #print("Best: ", best)

        return upperBound, current, best

upperBound, current, best = BnB(genomeObject, 0, 10, current, best)

best = best[:upperBound]
print("Final best: ",best)
print("Melano: ", melanoGenome)

genom = helpersSteven.GenomeSequence(melanoGenome)
for mutations in best:
    genom.genome = genom.Reverse(mutations[0], mutations[1])
print(genom.genome)

https://gyazo.com/b58c349ce6e56abe6fd3dff1dd5422cf
