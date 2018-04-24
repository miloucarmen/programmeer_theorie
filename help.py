def Options(genome, method):
    
    # find the breakpoints and positions
    breakpoints = FindBreakpoints(genome)
    unique = Breakpoint(breakpoints)

    options0 = []
    options1 = []
    options2 = []
    deltaPHIbest = 0
    # execute all possible reverses
    for i in unique:
        for j in unique:
            if i != j and i < j and i >= 1 and j <= 25:

                deltaPHI = calcDeltaPHI(genome, i, j, len(breakpoints))

                if method == "Greedy":
                    if deltaPHI >= deltaPHIbest:
                        if deltaPHI > deltaPHIbest:
                            deltaPHIbest = deltaPHI
                            options0 = []
                    options0.append((i,j))
                    # if deltaPHIbest is 2, and a descending strip was found
                    if testGenome[i-1] > testGenome[i] or testGenome[j + 1] < testGenome[j]:
                        if deltaPHIbest == 2:
                            return testGenome
                        if deltaPHIbest  ==  1 and options1 == []:
                            options1 = [i,j]
                
                else: 
                    #print(len(FindBreakpoints(genome)) - len(breakpoints))
                    if deltaPHI == 0:
                        options0.append((i,j))
                    elif deltaPHI == 1:
                        options1.append((i,j))
                    elif deltaPHI == 2:
                        options2.append((i,j))
    
    if method == "Greedy":
        if deltaPHIbest == 1:
        return Reverse(genome, bestOneBreakpoint[0], bestOneBreakpoint[1])
    else:    
        return options0, options1, options2 




          

def Breakpoint(breakpoints):

    unique = []
    for i in range(0, len(breakpoints)):
        for j in range(0, 2):
            if breakpoints[i][j] not in unique:
                unique.append(breakpoints[i][j])
    return unique


