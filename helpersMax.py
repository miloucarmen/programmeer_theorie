
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


def Mutate(genome, method):

    # declare arrays that store the breakpoint pairs that, when reversed,
    # eliminate either 0, 1, or 2 breakpoints in the genome
    #eliminate_0_breakpoints = []
    #eliminate_1_breakpoints = []
    #eliminate_2_breakpoints = []

    # declare an array that stores the options there are to mutate a gene
    # in the form ( i, j, deltaPHI, descending(T/F) )
    mutateOptions = []

    # set the best deltaPHI equal to 0
    deltaPHIbest = 0

    # find the pairs of breakpoints in the genome
    breakpointPairs = FindBreakpointPairs(genome)

    # find the positions of these breakpoint pairs
    breakpointPositions = FindBreakpointPositions(breakpointPairs)

    # find the number of breakpoints in the genome
    numberOfBreakpoints = len(breakpointPairs)

    # execute all possible reverses
    for i in breakpointPositions:
        for j in breakpointPositions:
            if i != j and i < j and i >= 1 and j <= 25:

                # execute every possible reverse and store the mutated genome
                # in temporaryGenome
                temporaryGenome = Reverse(genome, i, j)

                # count the number of breakpoints in the mutated genome
                numberOfBreakpointsNew = len(FindBreakpointPairs(temporaryGenome))

                # calculate the difference in PHI, incurred by the current mutation,
                # that is: mutating strip (i,j)
                deltaPHI = numberOfBreakpoints - numberOfBreakpointsNew

                if method == "Greedy":

                    # check whether deltaPHI is better/equally good as deltaPHIbest.
                    # If so, append it to the mutateOptions. If not, no need to
                    # store the option.
                    if deltaPHI >= deltaPHIbest:
                        if deltaPHI > deltaPHIbest:

                            # set the new deltaPHIbest if it is larger then the old one
                            deltaPHIbest = deltaPHI

                            # clear the mutateOptions to keep it small, because if a new
                            # deltaPHIbest has been found, we can throw away all old options
                            mutateOptions = []

                        # only consider deltaPHI = 2 and deltaPHI = 1, because for lower deltaPHIs
                        # you don't want to do anything
                        if deltaPHI == 2:

                            # check whether a descending strip was found
                            if temporaryGenome[i - 1] > temporaryGenome[i] or temporaryGenome[j] > temporaryGenome[j + 1]:

                                # if descending AND deltaPHI = 2, we've found our best option already!
                                return temporaryGenome

                            # if not descending, store the option and continue revising the
                            # other options
                            else:
                                mutateOptions.append((i, j, deltaPHI, False))

                        if deltaPHI == 1:

                            # check whether a descending strip was found
                            if temporaryGenome[i - 1] > temporaryGenome[i] or temporaryGenome[j] > temporaryGenome[j + 1]:

                                # if so, store the option and continue revising the
                                # other options
                                mutateOptions.append((i, j, deltaPHI, True))

                            # if not descending, store the option and continue revising the
                            # other options
                            else:
                                mutateOptions.append((i, j, deltaPHI, False))

                elif method == "B&B":
                    if deltaPHI == 0:
                        eliminate_0_breakpoints.append((i,j))
                    elif deltaPHI == 1:
                        eliminate_1_breakpoints.append((i,j))
                    elif deltaPHI == 2:
                        eliminate_2_breakpoints.append((i,j))

    # when all possible reverses are reviewed, let's see what we should do
    if method == "Greedy":

        # sort the mutateOptions array on deltaPHI. Using this sort method,
        # the lowest deltaPHIs come first (minimum 1) with FALSE booleans for
        # 'descending'.
        mutateOptions = sorted(mutateOptions, key = lambda x: (x[2], x[3]))

        # therefore, the array should be reversed
        mutateOptions = list(reversed(mutateOptions))

        # execute the first posssible option, because this is now the best one!
        # (because descending options come first in the array)
        return Reverse(genome, mutateOptions[0][0], mutateOptions[0][1])



# ----------- HIER MOET NOG NAAR GEKEKEN WORDEN. DIT IS VOOR DE B&B -----------
    # if method is B&B, return all options
    else:
        return eliminate_0_breakpoints, eliminate_1_breakpoints, eliminate_2_breakpoints

# ----------- HIER MOET NOG NAAR GEKEKEN WORDEN. DIT IS VOOR DE B&B -----------
def Greedy(genome):
    """Executes the Greedy algorithm"""

    mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    numberOfMutations = 0

    while genome != mirandaGenome:
        numberOfMutations += 1

        breakpoints = FindBreakpointPairs(genome)

        genome = Options(genome, "Greedy", breakpoints)

    return numberOfMutations