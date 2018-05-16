import helpersSteven_MAIL as helpers
from random import shuffle

# A function for making random mutations for testing purposes
def randomMutation(testLength):
    middleGenome = [i for i in range(1, testLength)]
    shuffle(middleGenome)
    return [0] + middleGenome + [testLength]

melanoGenome = randomMutation(7)
# [0, 2, 1, 25, 20, 19, 22, 23, 24, 11, 10, 7, 6, 5, 4, 3, 21, 17, 16, 15, 14, 13, 12, 18, 8, 9, 26]
i = 2
j = 4

mirandaGenome = [i for i in range(len(melanoGenome))]

print("The genome sequence eqals: ", melanoGenome)
print("The length of the genome equals: ", len(melanoGenome))

genomeObject = helpers.GenomeSequence(melanoGenome)

print("i equals: ", i)
print("j equals: ", j)

genomeObject.genome = genomeObject.Reverse(i,j)

print("Before updating the breakpointList is: ", genomeObject.breakpointList)

print("REVERSED: ", genomeObject.genome)

genomeObject.UpdateBreakpointList(i,j)
print("After updating the breakpointList is: ", genomeObject.breakpointList)



#print("The breakpoint pairs are: ", breakpointPairs)

# breakpointPositions = helpersMax.FindBreakpointPositions(breakpointPairs)
# print("The breakpoint positions are: ", breakpointPositions)

# reversedGenome = helpersMax.Reverse(genome, 3, 4)
# print("The reversed genome with i = 3 and j = 4: ", reversedGenome)

# print("The number of breakpoint pairs (i.e. breakpoints!) equals: ", len(breakpointPairs))

# mutateOptions = []
# mutateOptions.append((18, 19, 2, True))
# mutateOptions.append((4, 16, 2, False))
# mutateOptions.append((1, 3, 1, False))
# mutateOptions.append((7, 10, 1, True))
# print(mutateOptions)

# sortedArray = sorted(mutateOptions, key = lambda x: (x[2], x[3]))
# print(sortedArray)

# sortedArray = list(reversed(sortedArray))
# print(sortedArray)
