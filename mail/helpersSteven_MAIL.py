import math
import scipy

# we moeten in de presentatie goed onderbouwen dat een strip doorbreken NOOIT goed is, ik twijfel hierover?
class GenomeSequence:

    def __init__(self, genome):

        self.genome = genome
        # execute createBreakpointlist when initializing
        self.breakpointList, self.breakpointPairs = self.createBreakpointList(genome)

    def createBreakpointList(self, genome):
        # declare arrays that store indices that may be an i or a j
        breakpointList = []
        breakpointPairs = 0
        for i in range(0, len(genome) - 1):
            # check if breakpoint
            if abs(genome[i] - genome[i + 1]) != 1:
                breakpointPairs = breakpointPairs + 1
                # specify what may be a possible i or j
                if i > 0 and i < len(genome) - 1:
                    breakpointList.append(i)
                if i < len(genome) - 2:
                    breakpointList.append(i + 1)

        breakpointList = list(set(breakpointList))

        # print("initial", breakpointList)

        return breakpointList, breakpointPairs

    def UpdateBreakpointList(self, i, j):
        # https://gyazo.com/9389e6324f980a2bee57a173f5358a91  <--- dit geval eruit halen
        # print("old", self.breakpointList)
        newList = []

        for m in [i - 1, i, j, j + 1]:
            if abs(self.genome[m - 1] - self.genome[m]) == 1:
                if m < len(self.genome) - 1:
                    if m in self.breakpointList and m not in newList:
                        self.breakpointList.remove(m)

                if m - 1 > 0:
                    if m - 1 in self.breakpointList and m - 1 not in newList:
                        if m - 2 >= 0 and abs(self.genome[m - 2] - self.genome[m - 1]) == 1:
                            self.breakpointList.remove(m - 1)
            else:
                if m - 1 > 0:
                    self.breakpointList.append(m - 1)
                    newList.append(m - 1)
                if m > 0:
                    self.breakpointList.append(m)
                    newList.append(m)

            if m + 1 < len(self.genome):
                if abs(self.genome[m] - self.genome[m + 1]) == 1:
                    if m in self.breakpointList and m not in newList:

                        self.breakpointList.remove(m)
                    if m + 1 in self.breakpointList and m + 1 not in newList:
                        if m + 2 < len(self.genome) and abs(self.genome[m + 2] - self.genome[m + 1]) == 1:
                            self.breakpointList.remove(m + 1)
                else:
                    if m + 1 < len(self.genome) - 1:
                        self.breakpointList.append(m + 1)
                        newList.append(m + 1)
                    self.breakpointList.append(m)
                    newList.append(m)


        self.breakpointList = list(set(self.breakpointList))
        # print("new", self.breakpointList)


    def CalcDeltaPHI(self, i, j):

        # define bools to check if breakpoints are eliminated
        eliminatedLeftBreakpoint = 0
        eliminatedRightBreakpoint = 0
        breakleftStrip = 0
        breakrightStrip = 0

        if abs(self.genome[i - 1] - self.genome[i]) == 1:
            breakleftStrip = -1

        if abs(self.genome[j + 1] - self.genome[j]) == 1:
            breakrightStrip = -1

        # check if left breakpoint will be eliminated when reversing with
        # indices i and j
        if abs(self.genome[i - 1] - self.genome[j]) == 1:
            eliminatedLeftBreakpoint = 1

        # check if right breakpoint will be eliminated when reversing with
        # indices i and j
        if abs(self.genome[j + 1] - self.genome[i]) == 1:
            eliminatedRightBreakpoint = 1

        # return the sum of the bools to get the total number of breakpoints
        # that will be eliminated when reversing with indices i and j (this number will
        # always be either 0, 1 or 2)
        return eliminatedLeftBreakpoint + eliminatedRightBreakpoint + breakleftStrip + breakrightStrip


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


    # def trimOptionsLow(self, currentIndex):
    #     if currentIndex < len(self.breakpointList):
    #         if self.genome[currentIndex] == currentIndex:
    #             self.trimOptionsLow(currentIndex + 1)
    #             del self.breakpointList[self.breakpointList.index(currentIndex)]

    # def trimOptionsHigh(self, currentIndex):
    #     if currentIndex > 0:
    #         if self.genome[currentIndex] == currentIndex:
    #             self.trimOptionsHigh(currentIndex - 1)
    #             del self.breakpointList[self.breakpointList.index(currentIndex)]

    def Mutate(self, method):

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
        # print(self.breakpointList)
        # execute all possible reverses, based on the possible Is and Js

        # print("Breakpointlist before trim: ", self.breakpointList)
        # self.trimOptionsLow(1)
        # self.trimOptionsHigh(len(self.breakpointList) - 1)
        
        for i in self.breakpointList:
            for j in self.breakpointList:
                if i != j and i < j and i >= 1 and j < len(self.genome) - 1:

                    # execute every possible reverse and store the mutated genome
                    # in temporaryGenome and calculate the difference in PHI, incurred by the current mutation,
                    # that is: mutating strip (i,j)
                    temporaryGenome = self.Reverse(i, j)
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
            return self.Reverse(mutateOptions[0][0], mutateOptions[0][1])



        # if method is B&B, return all options
        else:
            # print("return", eliminate_2_breakpoint, eliminate_1_breakpoint, eliminate_0_breakpoint)
            return eliminate_2_breakpoint, eliminate_1_breakpoint, eliminate_0_breakpoint#, eliminate_min_1_breakpoint, eliminate_min_2_breakpoint

    # def UpdateIandJ(self, i, j):
    #     print("Is", self.Is)
    #     print("Js", self.Js)
    #     print("j", j)
    #     for k in self.Is[self.Is.index(i):]:
    #         offset = 0
    #         if k > i:
    #             self.Js.append(k)
    #             self.Is.remove(k)
    #             offset =+ 1
    #         elif k == self.Js.index(j - offset):
    #             break

    #         self.Is = list(set(self.Is))
    #         self.Js = list(set(self.Js))

    #     for l in self.Js[self.Is.index(i):]:
    #         offset = 0
    #         if l > i:
    #             self.Is.append(l)
    #             self.Js.remove(l)
    #             offset =+ 1
    #         elif l == self.Js.index(j - offset):
    #             break

    #         self.Is = list(set(self.Is))
    #         self.Js = list(set(self.Js))

    #     for m in [i - 1, i, j, j + 1]:
    #         if abs(self.genome[m - 1] - self.genome[m]) == 1:
    #             if m in self.Is:
    #                 self.Is.remove(m)
    #             if m - 1 in self.Js:
    #                 self.Js.remove(m - 1)
    #         else:
    #             self.Js.append(m - 1)
    #             self.Is.append(m)
    #         if self.genome[m] != self.genome[-1]:
    #             if abs(self.genome[m + 1] - self.genome[m]) == 1:
    #                 if m + 1 in self.Is:
    #                     self.Is.remove(m + 1)
    #                 if m in self.Js:
    #                     self.Js.remove(m)
    #             else:
    #                 self.Js.append(m)
    #                 self.Is.append(m + 1)

    #     self.Is = list(set(self.Is))
    #     self.Js = list(set(self.Js)) # checken of duplicates hiervan wegkunnen

    def Greedy(self, genome):
        """Executes the Greedy algorithm"""

        print("GREEDY!")

        # mirandaGenome is the genome in ascending order
        mirandaGenome = [i for i in range(len(genome))]

        numberOfMutations = 0

        # while genome != mirandaGenome:
        #     numberOfMutations += 1
        #     genome = self.Mutate(genome, "Greedy")
        #     print(genome)

        return numberOfMutations

    def lowerBoundPoints(self):
        scipy.spatial.distance.cdist

def LowerBound(breakpointpairsCurrent):
    return math.ceil(breakpointpairsCurrent / 2)
