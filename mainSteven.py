import helpersSteven

def main():

    # the genome has a length of 25 EXCLUDING the 0 and 26 on the ends.
    # the 0 and the 26 on the ends are used to recognize if the first and last gen
    # are on the right spot
    melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
    mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    # keep track of the number of mutations
    numberOfMutations = 0

    # set 'genome' for the very first start equal to the melanoGenome
    # 'genome' will be mutating
    genome = helpersSteven.GenomeSequence(melanoGenome)

    # these are all the attributes of genome
    #print(vars(genome))

    # keep mutating while 'genome' does not equal our objective genome (Miranda)!
    while genome.genome != mirandaGenome:
        """The mutation loop"""

        # increment the number of mutations on each loop
        numberOfMutations += 1

        # mutate the genome
        genome = genome.Mutate("Greedy")
        genome = helpersSteven.GenomeSequence(genome)
        print(genome.genome)

    print(numberOfMutations)

if __name__ == "__main__":
    main()



    #  def Update(self, genome, i, j):

    #     # breakpointPairs, self.breakpointPostions, self.Is, self.Js = self.createBreakpointList(genome)

    #     mutatedGenome = self.Mutate(genome, i, j)
    #     # ittereerd door breakpoints
    #     for q in range(j + 1):
    #         if self.breakpointPostions[q] > i and self.breakpointPostions[q] < j:
    #             # veranderd breakpointpostions naar hun nieuwe locatie
    #             self.breakpointPostions[q]  = j - q + i
    #         if self.breakpointPostions[q] == i:
    #             if abs(mutatedGenome[i-1] - mutatedGenome[i-2]) == 1 and abs(mutatedGenome[i] - mutatedGenome[i - 1]) == 1:
    #                 self.breakpointPostions.remove[q - 1]
