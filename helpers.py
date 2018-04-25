
def FindBreakpointPairs(genome):
    """Finds all breakpoint pairs in a given genome"""

    breakpointPairs = []
    for i in range(0, len(genome) - 1):
        if abs(genome[i] - genome[i + 1]) != 1:
            breakpointPairs.append((i, i + 1))

    return breakpointPairs


def FindBreakpointPositions(breakpointPairs):
    """Finds the indices (positions) of the genes in the genome that
        participate in the breakpoint pairs"""

    breakpointPositions = []
    for i in range(0, len(breakpointPairs)):
        for j in range(0, 2):
            if breakpointPairs[i][j] not in breakpointPositions:
                breakpointPositions.append(breakpointPairs[i][j])

    return breakpointPositions


def Reverse(genome, i, j):
    """Reverses a strip with begin index i and end index j in a given genome"""

    # the first piece of the genome
    genomeStart = genome[0 : i]
    #print(genomeStart)

    # the to be mutated part in the genome
    genomeMutation = genome[i : j + 1]
    #print(genomeMutation)

    # the to be mutated part reversed
    genomeMutated = list(reversed(genomeMutation))
    #print(genomeMutated)

    # the ending part of the genome
    genomeEnd = genome[j + 1 : len(genome)]
    #print(genomeEnd)

    # return the mutated genome
    return genomeStart + genomeMutated + genomeEnd


def Options(genome, method, breakpoints):

    options0 = []
    options1 = []
    options2 = []

    deltaPHIbest = 0

    breakpointPositions = FindBreakpointPositions(breakpoints)
    numberOfBreakpoints = len(FindBreakpointPairs(genome))

    # execute all possible reverses
    for i in breakpointPositions:
        for j in breakpointPositions:
            if i != j and i < j and i >= 1 and j <= 25:

                temporaryGenome = Reverse(genome, i, j)

                numberOfBreakpointsNew = len(FindBreakpointPairs(temporaryGenome))

                # calculate the difference in PHI, incurred by mutating strip (i,j)
                deltaPHI = numberOfBreakpoints - numberOfBreakpointsNew

                print(deltaPHI)
                print(genome)
                if method == "Greedy":
                    if deltaPHI >= deltaPHIbest:
                        if deltaPHI > deltaPHIbest:
                            deltaPHIbest = deltaPHI
                            options0 = []
                        options0.append((i,j))

                    # check whether a descending strip was found
                    if temporaryGenome[i-1] > temporaryGenome[i] or temporaryGenome[j + 1] < temporaryGenome[j]:

                        # if descending strip has been found and 2 breakpoints
                        # are eliminated, we've found our best option already!
                        if deltaPHIbest == 2:
                            return temporaryGenome

                        # if descending strip has been found and 1 breakpoint
                        # can be cancelled, save the option
                        if deltaPHIbest  ==  1 and options1 == []:
                            options1.append((i,j))

                elif method == "B&B":
                    if deltaPHI == 0:
                        options0.append((i,j))
                    elif deltaPHI == 1:
                        options1.append((i,j))
                    elif deltaPHI == 2:
                        options2.append((i,j))

    if method == "Greedy":

        # if best option is to eliminate 1 breakpoint and the strip is descending
        # do this option
        if deltaPHIbest == 1 and options1 != None:
            return Reverse(genome, options1[0][0], options1[0][1])

        # otherwise execute the first option available
        return Reverse(genome, options0[0][0], options0[0][1])

    # if method is B&B, return all options
    else:
        return options0, options1, options2


def Greedy(genome):
    """Executes the Greedy algorithm"""

    mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    numberOfMutations = 0

    while genome != mirandaGenome:
        numberOfMutations += 1

        breakpoints = FindBreakpointPairs(genome)

        genome = Options(genome, "Greedy", breakpoints)

    return numberOfMutations