# we moeten in de presentatie goed onderbouwen dat een strip doorbreken NOOIT goed is, ik twijfel hierover? 
class GenomeSequence:
    def __init__(self, genome):
        self.genome = genome
        # self.breakpoints eigenlijk overbodig, maar gaat nog handig zijn bij die 2x sneller comment?
        self.breakPointsList, self.breakPoints, self.breakPointsPostions = self.createBreakpointList(genome)

    def createBreakpointList(self, genome):
        breakPointsList = [[0, 0]] * len(genome)
        breakPoints = []
        breakPointsPositions = []
        for i in range(len(genome)):
            if i == 0:
                breakPointsList[i][1] = genome[i + 1]
                if genome[i + 1] != 1:
                    breakPoints.append((i, i + 1))
                    breakPointsPositions.append(genome[i])
                    breakPointsPositions.append(genome[i + 1])

            elif i == len(genome):
                breakPointsList[i][0] = genome[i - 1]

            else:
                breakPointsList[i] = [genome[i - 1], genome[i + 1]]
                if abs(genome[i] - genome[i + 1]) != 1:
                    breakPoints.append((i, i + 1))
                    for j in range(2):
                        if breakPoints[i][j] not in breakPointsPositions:
                            breakPointsPositions.append(breakPoints[i][j])

        return breakPointsList, breakPoints, breakPointsPositions


    def updateBreakpoints(self, i, j):
        oldPHIOne, oldPhiTwo, newPHIOne, newPhiTwo = 0

        if abs(self.breakPointsList[i] - self.breakPointsList[i - 1]) != 1:
            oldPHIOne = 1
        if abs(self.breakPointsList[j] - self.breakPointsList[j + 1]) != 1:
            oldPHITwo = 1


        # als sort te langzaam is, hier oplossen 
        temp =  self.breakPointsList[i - 1][1] = j
        self.breakPointsList[j + 1][0] = i
        tempVar = self.breakPointsList[i][0]
        self.breakPointsList[i][0] = self.breakPointsList[j][1]
        self.breakPointsList[j][1] = tempVar
        self.breakPointsList[i - 1][1] = j
        self.breakPointsList[j + 1][0] = i
        tempVar = self.breakPointsList[i][0]
        self.breakPointsList[i][0] = self.breakPointsList[j][1]
        self.breakPointsList[j][1] = tempVar

        if abs(self.breakPointsList[i] - self.breakPointsList[i - 1]) != 1:
            newPHIOne = 1
        if abs(self.breakPointsList[j] - self.breakPointsList[j + 1]) != 1:
            newPHITwo = 1

        # if oldPHIOne - newPHIOne == 1:
        


        
        return sum(oldPHIOne, oldPhiTwo) - sum(newPHIOne, newPhiTwo)
        

    def Reverse(self, genome, i, j):
        """Reverses a strip with begin index i and end index j in a given genome"""

        # the first piece of the genome
        genomeStart = genome[0 : i]

        # the to be mutated part in the genome
        genomeMutation = genome[i : j + 1]

        # the to be mutated part reversed
        genomeMutated = list(reversed(genomeMutation))

        # the ending part of the genome
        genomeEnd = genome[j + 1 : len(genome)]

        deltaPHI = self.updateBreakpoints(i, j)
        # return the mutated genome
        return genomeStart + genomeMutated + genomeEnd, deltaPHI


    def Mutate(self, genome, method):

        # declare arrays that store the breakpoint pairs that, when reversed,
        # eliminate either 0, 1, or 2 breakpoints in the genome
        eliminate_0_breakpoints = []
        eliminate_1_breakpoints = []
        eliminate_2_breakpoints = []
        eliminate_min_1_breakpoints = []
        eliminate_min_2_breakpoints = []

        # declare an array that stores the options there are to mutate a gene
        # in the form ( i, j, deltaPHI, descending(T/F) )
        mutateOptions = []

        # set the best deltaPHI equal to 0
        deltaPHIbest = 0

        # execute all possible reverses
        for i in self.breakPointsPostions:
            for j in self.breakPointsPostions:
                # CODE KAN HIER NOG 2X ZO SNEL WORDEN GEMAAKT DOOR TE CHECKEN AAN WELKE KANT DE STRIPT ISSSSSSSSSSSS
                if i != j and i < j and i >= 1 and j <= len(genome) - 2:

                    # execute every possible reverse and store the mutated genome
                    # in temporaryGenome and calculate the difference in PHI, incurred by the current mutation,
                    # that is: mutating strip (i,j)
                    temporaryGenome = self.Reverse(genome, i, j)
                    deltaPHI = 

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

                            if deltaPHI == 0:

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
                        # elif deltaPHI == -1:
                        #     eliminate_min_1_breakpoints.append((i,j))
                        # elif deltaPHI == -2:
                        #     eliminate_min_2_breakpoints.append((i,j))

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
            return self.Reverse(genome, mutateOptions[0][0], mutateOptions[0][1])



    # ----------- HIER MOET NOG NAAR GEKEKEN WORDEN. DIT IS VOOR DE B&B -----------
        # if method is B&B, return all options
        else:
            return eliminate_2_breakpoints, eliminate_1_breakpoints, eliminate_0_breakpoints, eliminate_min_1_breakpoints, eliminate_min_2_breakpoints

    # ----------- HIER MOET NOG NAAR GEKEKEN WORDEN. DIT IS VOOR DE B&B -----------
    def Greedy(self, genome):
        """Executes the Greedy algorithm"""
        mirandaGenome = [i for i in range(len(genome))]
        # mirandaGenome = [0,1,2,3,4]
        numberOfMutations = 0

        while genome != mirandaGenome:
            numberOfMutations += 1
            genome = self.Mutate(genome, "Greedy")

        return numberOfMutations

    def LowBound(self, genome):
        return int(len(self.breakPointsPostions) / 2)