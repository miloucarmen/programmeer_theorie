def main():
    # the genome has a length of 25 EXCLUDING the 0 and 26 on the ends.
    #melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]

    melanoGenome = [0, 2, 1, 25, 20, 19, 22, 23, 24, 11, 10, 7, 6, 5, 4, 3, 21, 17, 16, 15, 14, 13, 12, 18, 8, 9, 26]


    mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    numberOfMutations = 0
    genome = melanoGenome

    while genome != mirandaGenome:
        numberOfMutations += 1
        print("Mutate wordt aangeroepen")
        genome = Mutate(genome)
        print(genome)
    print(numberOfMutations)


def FindBreakpoints(genome):
    """Find the number of breakpoints"""
    breakPoints = []
    for i in range(0,26):
        if abs(genome[i] - genome[i + 1]) != 1:
            breakPoints.append((i, i + 1))

    return breakPoints

def Reverse(genome, i, j):
    genomeStart = genome[0 : i]
    #print(genomeStart)
    genomeMutation = genome[i : j + 1]
    #print(genomeMutation)
    genomeMutated = list(reversed(genomeMutation))
    #print(genomeMutated)
    genomeEnd = genome[j + 1 : len(genome)]
    #print(genomeEnd)
    return genomeStart + genomeMutated + genomeEnd

def Mutate(genome):
    print("Aangekomen in Mutate()")
    breakpoints = FindBreakpoints(genome)

    # find the breakpoint positions
    unique = []
    for i in range(0, len(breakpoints)):
        for j in range(0, 2):
            if breakpoints[i][j] not in unique:
                unique.append(breakpoints[i][j])

    deltaPHIbest = 0
    print("deltaPHIbest is gezet op 0")
    options = []
    bestOneBreakpoint = []

    # execute all possible reverses
    for i in unique:
        for j in unique:
            if i != j and i < j and i >= 1 and j <= 25:
                print(bestOneBreakpoint)
                #print(i, j)
                testGenome = Reverse(genome, i, j)
                print("Er is een testGenome gemaakt")
                breakpointsNew = FindBreakpoints(testGenome)
                print("Het nieuwe aantal breakpoints = ", len(breakpointsNew))
                breakpointsOld = FindBreakpoints(genome)
                print("Het oude aantal breakpoints = ", len(breakpointsOld))
                deltaPHI = len(breakpointsOld) - len(breakpointsNew)
                print("delta PHI is dus: ", deltaPHI)

                if deltaPHI >= deltaPHIbest:
                    if deltaPHI > deltaPHIbest:
                        deltaPHIbest = deltaPHI
                        print("Een nieuwe BEST is aangesteld: ", deltaPHIbest)
                        options = []
                    options.append((i,j))
                    print("De nieuwe lijst met options is: ", options)
                    print("Het huidige genome is: ", genome)

                # if deltaPHIbest is 2, and a descending strip was found
                if testGenome[i-1] > testGenome[i] or testGenome[j + 1] < testGenome[j]:
                    print("Er is een descending strip gevonden")
                    if deltaPHIbest == 2:
                        print("En hij was ook met 2 reversals, dus voer hem uit!")
                        return testGenome
                    if deltaPHIbest  ==  1 and bestOneBreakpoint == []:
                        print("bestOneBreakpoint wordt gemaakt!")
                        bestOneBreakpoint = [i,j]

    # als er geen deltaPHIbest == 2 is gevonden, maar wel een descending order bij deltaPHIbest == 1
    if deltaPHIbest == 1:
        print("We hebben alle opties bekeken, en BEST is nog steeds maar 1")
        return Reverse(genome, bestOneBreakpoint[0], bestOneBreakpoint[1])

    # if deltaPHIbest is 1 or 2, but no descending strip was found. Get the first one, because why not? All options in 'option' have deltaPHI == 2.
    print("Er is GEEN descending strip gevonden, dus pak de eerste optie??????")
    return Reverse(genome, options[0][0], options[0][1])


if __name__ == "__main__":
    main()
    # i moet altijd >= 1 en j moet altijd <= 25!

# er zijn 17 breakpoints binnen het genoom hoe vaak doe je een swap die twee breakpoint weg haalt.
# Ze gaan er vanuit dat elke stap 2 breakpoints weg haalt vandaar gedeeld door.