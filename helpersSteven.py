# we moeten in de presentatie goed onderbouwen dat een strip doorbreken NOOIT goed is, ik twijfel hierover?
class GenomeSequence:
    def __init__(self, genome):
        self.genome = genome
        # self.breakpointPairs eigenlijk overbodig, maar gaat nog handig zijn bij die 2x sneller comment?
        self.neighbouringNumbers, self.breakpointPairs, self.breakpointPostions, self.Is, self.Js = self.createBreakpointList(genome)

    def createBreakpointList(self, genome):

        # neighbouringNumbers stores the pair of neighbouring numbers for each gen in a given genome
        #neighbouringNumbers = [(0, 0)] * (len(genome) + 1)

        # breakpointPairs stores all breakpoint pairs in a given genome"""
        breakpointPairs = []

        # breakpointPositions stores the indices (positions) of the genes in the genome that
        # participate in the breakpoint pairs
        breakpointPositions = []

        # declare arrays that store indices that may be an i or a j
        Is = []
        Js = []

        # declare an offset for the index i
        offSet = 0

        for i in range(len(genome) + 1):
            print("i equals: ", i)

            # for the first element considered
            if i == 0:

                # only change the 1st element, because 0th already is 0
                #neighbouringNumbers[i][1] = genome[i + 1]

                # IF a breakpoint, store the breakpoint's information
                if genome[i + 1] != 1:
                    breakpointPairs.append((i, i + 1))
                    breakpointPositions.append(genome[i])
                    breakpointPositions.append(genome[i + 1])
                    Is.append(i + 1)

                # if not a breakpoint, add one from the offset
                else:
                    offSet += 1

            # for the last element considered
            #elif i == len(genome) - 1:

                # only change the 0th element, because 1st already is 0
                #neighbouringNumbers[i][0] = genome[i - 1]

            # for all other elements
            else:
                # store the neighbouring elements
                #neighbouringNumbers[i] = [genome[i - 1], genome[i + 1]]

                # check if a breakpoint
                if abs(genome[i] - genome[i + 1]) != 1:

                    # specify what may be a possible i or j
                    Js.append(i)
                    Is.append(i + 1)

                    # store the information of the breakpoints
                    breakpointPairs.append((i, i + 1))
                    for j in range(2):
                        print("i equals: ", i, "j equals: ", j)
                        print(breakpointPairs)

                        # here we use the offSet
                        if breakpointPairs[i - offSet][j] not in breakpointPositions:
                            breakpointPositions.append(breakpointPairs[i - offSet][j])

                # if not a breakpoint, add one from the offset
                else:
                    offSet += 1

        return breakpointPairs, breakpointPositions, Is, Js #, neighbouringNumbers



    def CheckPHI(self, i, j):
        oldPHIOne, oldPhiTwo, newPHIOne, newPhiTwo = 0

        if abs(genome[i - 1] - genome[i]) != 1:
            oldPHIOne = 1
        if abs(genome[j + 1] - genome[j]) != 1:
            oldPHITwo = 1

        if abs(genome[i - 1] - genome[j]) != 1:
            newPHIOne = 1
        if abs(genome[j + 1] - genome[i]) != 1:
            newPHITwo = 1

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

        # declare arrays that store the breakpointPairs pairs that, when reversed,
        # eliminate either 0, 1, or 2 breakpointPairs in the genome
        eliminate_0_breakpoint = []
        eliminate_1_breakpoint = []
        eliminate_2_breakpoint = []
        eliminate_min_1_breakpoint = []
        eliminate_min_2_breakpoint = []

        # declare an array that stores the options there are to mutate a gene
        # in the form ( i, j, deltaPHI, descending(T/F) )
        mutateOptions = []

        # set the best deltaPHI equal to 0
        deltaPHIbest = 0

        # execute all possible reverses, based on the possible Is and Js
        for i in self.Is:
            for j in self.Js:
                if i != j and i < j and i >= 1 and j <= len(genome) - 2:

                    # execute every possible reverse and store the mutated genome
                    # in temporaryGenome and calculate the difference in PHI, incurred by the current mutation,
                    # that is: mutating strip (i,j)
                    temporaryGenome = self.Reverse(genome, i, j)
                    deltaPHI = self.CheckPHI(i, j)

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
                            eliminate_0_breakpoint.append((i,j))
                        elif deltaPHI == 1:
                            eliminate_1_breakpoint.append((i,j))
                        elif deltaPHI == 2:
                            eliminate_2_breakpoint.append((i,j))
                        # elif deltaPHI == -1:
                        #     eliminate_min_1_breakpoint.append((i,j))
                        # elif deltaPHI == -2:
                        #     eliminate_min_2_breakpoint.append((i,j))

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
            return eliminate_2_breakpoint, eliminate_1_breakpoint, eliminate_0_breakpoint, eliminate_min_1_breakpoint, eliminate_min_2_breakpoint

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
        return int(len(self.breakpointPostions) / 2)