# we moeten in de presentatie goed onderbouwen dat een strip doorbreken NOOIT goed is, ik twijfel hierover?
class GenomeSequence:

    def __init__(self, genome):

        self.genome = genome

        # execute createBreakpointlist when initializing
        self.breakpointPairs, self.breakpointPostions, self.Is, self.Js = self.createBreakpointList(genome)

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

        for i in range(len(genome) - 1):
            print("i equals: ", i)

            # check if breakpoint
            if abs(genome[i] - genome[i + 1]) != 1:

                # add the breakpoint pair to the list
                breakpointPairs.append((i, i + 1))

                # check if the breakpoint position is already stored. If not, add it to the
                # breakpointPositions list
                if breakpointPairs[len(breakpointPairs) - 1][0] not in breakpointPositions:
                    breakpointPositions.append(i)
                if breakpointPairs[len(breakpointPairs) - 1][1] not in breakpointPositions:
                    breakpointPositions.append(i + 1)

                # specify what may be a possible i or j
                Js.append(i)
                Is.append(i + 1)

        print("breakpointPairs: ", breakpointPairs)
        print("breakpointPositions: ", breakpointPositions)
        print("I's: ", Is)
        print("J's: ", Js)
        return breakpointPairs, breakpointPositions, Is, Js #, neighbouringNumbers


    def CalcDeltaPHI(self, i, j):

        # define bools to check if breakpoints are eliminated
        eliminatedLeftBreakpoint = False
        eliminatedRightBreakpoint = False

        # check if left breakpoint will be eliminated when reversing with
        # indices i and j
        if abs(self.genome[i - 1] - self.genome[j]) == 1:
            eliminatedLeftBreakpoint = True

        # check if right breakpoint will be eliminated when reversing with
        # indices i and j
        if abs(self.genome[j + 1] - self.genome[i]) == 1:
            eliminatedRightBreakpoint = True

        print(eliminatedLeftBreakpoint + eliminatedRightBreakpoint)

        # return the sum of the bools to get the total number of breakpoints
        # that will be eliminated when reversing with indices i and j (this number will
        # always be either 0, 1 or 2)
        return eliminatedLeftBreakpoint + eliminatedRightBreakpoint


    def Reverse(self, i, j):
        """Reverses a strip with begin index i and end index j in a given genome"""

        # the first piece of the genome
        genomeStart = self.genome[0 : i]

        # the to be mutated part in the genome
        genomeMutation = self.genome[i : j + 1]

        # the to be mutated part reversed
        genomeMutated = list(reversed(genomeMutation))

        # the ending part of the genome
        genomeEnd = self.genome[j + 1 : len(self.genome)]

        # return the mutated genome
        return genomeStart + genomeMutated + genomeEnd


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
                    deltaPHI = self.CalcDeltaPHI(i, j)

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