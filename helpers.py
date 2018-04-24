
def FindBreakpoints(genome):
    """Finds all breakpoint pairs in a given genome"""

    breakpoints = []
    for i in range(0, len(genome) - 1):
        if abs(genome[i] - genome[i + 1]) != 1:
            breakpoints.append((i, i + 1))

    return breakpoints


def FindBreakpointPositions(breakpoints)
    """Finds the indices (positions) of the genes in the genome that
        participate in the breakpoint pairs"""

    breakpointPositions = []
    for i in range(0, len(breakpoints)):
        for j in range(0, 2):
            if breakpoints[i][j] not in breakpointPositions:
                breakpointPositions.append(breakpoints[i][j])


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

    # execute all possible reverses
    for i in breakpointsPositions:
        for j in breakpointsPositions:
            if i != j and i < j and i >= 1 and j <= 25:

                temporaryGenome = Reverse(genome, i, j)

                numberOfBreakpointsNew = len(FindBreakpoints(temporaryGenome))

                # calculate the difference in PHI, incurred by mutating strip (i,j)
                deltaPHI = numberOfBreakpoints - numberOfBreakpointsNew

                if method == "Greedy":
                    if deltaPHI >= deltaPHIbest:
                        if deltaPHI > deltaPHIbest:
                            deltaPHIbest = deltaPHI
                            options0 = []
                    options0.append((i,j))

                    # if deltaPHIbest is 2, and a descending strip was found
                    if temporaryGenome[i-1] > temporaryGenome[i] or temporaryGenome[j + 1] < temporaryGenome[j]:
                        if deltaPHIbest == 2:
                            return temporaryGenome
                        if deltaPHIbest  ==  1 and options1 == []:
                            options1 = [i,j]

                elif method == "B&B":
                    if deltaPHI == 0:
                        options0.append((i,j))
                    elif deltaPHI == 1:
                        options1.append((i,j))
                    elif deltaPHI == 2:
                        options2.append((i,j))

    if method == "Greedy":

        # bestonebreak moet worden aangepast en de return gecontroleerd worden
        if deltaPHIbest == 1 and options1 != null:
           return Reverse(genome, options1[0], options1[1])
        return Reverse(genome, options0[0][0], options0[0][1])
    else:
        return options0, options1, options2




def ExecuteOptions(breakpointsPositions, deltaPHIbest):
    """Executes all possible reverses"""

    options = []

    for i in breakpointsPositions:
        for j in breakpointsPositions:
            if i != j and i < j and i >= 1 and j <= 25:

                temporaryGenome = Reverse(genome, i, j)

                numberOfBreakpointsNew = len(FindBreakpoints(temporaryGenome))

                # calculate the difference in PHI, incurred by mutating strip (i,j)
                deltaPHI = numberOfBreakpoints - numberOfBreakpointsNew

                # if the currently found deltaPHI is larger than deltaPHIbest, clear
                # options and redefine deltaPHIbest
                if deltaPHI > deltaPHIbest:
                    deltaPHIbest = deltaPHI
                    options = []

                # if the currently found deltaPHI equals deltaPHIbest, append this option
                # to the option list
                elif deltaPHI == deltaPHIbest:
                    options.append((i,j))


                # check if a descending strip was found
                if testGenome[i-1] > testGenome[i] or testGenome[j + 1] < testGenome[j]:

                    # if deltaPHIbest equals 2, we've found our best option already!
                    if deltaPHIbest == 2:
                        return testGenome

                    #
                    if deltaPHIbest  ==  1 and bestOneBreakpoint == []:
                        bestOneBreakpoint = [i,j]



def Mutate(genome, method):

    # find the breakpoint pairs
    breakpoints = FindBreakpoints(genome)

    # calculate the number of breakpoints
    numberOfBreakpoints = len(breakpoints)

    # find the positions (indices) of the genes participating in the breakpoint pairs
    breakpointsPositions = FindBreakpointsPositions(breakpoints)

    deltaPHIbest = 0
    bestOneBreakpoint = []

    ExecuteOptions(breakpointsPositions, deltaPHIbest)

    # execute all possible reverses
    for i in unique:
        for j in unique:
            if i != j and i < j and i >= 1 and j <= 25:

                # calculate the difference in PHI, incurred by mutating strip (i,j)
                deltaPHI = CalcDeltaPHI(genome, i, j, numberOfBreakpoints)

                if deltaPHI >= deltaPHIbest:
                    if deltaPHI > deltaPHIbest:
                        deltaPHIbest = deltaPHI
                        options = []
                    options.append((i,j))

                # print(options)
                # print(deltaPHIbest)

                # if deltaPHIbest is 2, and a descending strip was found
                if testGenome[i-1] > testGenome[i] or testGenome[j + 1] < testGenome[j]:
                    if deltaPHIbest == 2:
                        return testGenome
                    if deltaPHIbest  ==  1 and bestOneBreakpoint == []:
                        bestOneBreakpoint = [i,j]

    # als er geen deltaPHIbest == 2 is gevonden, maar wel een descending order bij deltaPHIbest == 1
    if deltaPHIbest == 1:
        return Reverse(genome, bestOneBreakpoint[0], bestOneBreakpoint[1])


    # if deltaPHIbest is 1 or 2, but no descending strip was found. Get the first one, because why not? All options in 'option' have deltaPHI == 2.
    return Reverse(genome, options[0][0], options[0][1])